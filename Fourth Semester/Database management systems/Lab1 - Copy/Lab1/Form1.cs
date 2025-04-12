using System;
using System.Configuration;
using System.Data;
using System.Windows.Forms;
using System.Data.SqlClient;
using System.Diagnostics;
using System.Linq;

namespace Lab1
{
    public partial class Form1 : Form
    {
        static string con = ConfigurationManager.ConnectionStrings["cn"].ConnectionString;

        static string parentName = ConfigurationManager.AppSettings["parentTable"];
        static string childName = ConfigurationManager.AppSettings["childTable"];
        static int childNumberOfColumns = int.Parse(ConfigurationManager.AppSettings["childNumberOfColumns"]);
        static string insert = ConfigurationManager.AppSettings["childInsert"];
        static string update = ConfigurationManager.AppSettings["childUpdate"];
        static string delete = ConfigurationManager.AppSettings["childDelete"];

        static string childArr = ConfigurationManager.AppSettings["childArr"];

        static string childColumnNames = ConfigurationManager.AppSettings["childColumnNames"];
        static string childColumnTypes = ConfigurationManager.AppSettings["childColumnTypes"];
        static string childToParentID = ConfigurationManager.AppSettings["childToParentID"];

        SqlConnection cs = new SqlConnection(con);

        SqlDataAdapter da = new SqlDataAdapter();

        DataSet dsParent = new DataSet();
        DataSet dsChild = new DataSet();

        BindingSource bsParent = new BindingSource();
        BindingSource bsChild = new BindingSource();

        TextBox[] textBoxes = new TextBox[childNumberOfColumns];
        Label[] labels = new Label[childNumberOfColumns];

        public Form1()
        {
            InitializeComponent();
            GenerateFormFieldsFromConfig();
        }

        private void GenerateFormFieldsFromConfig()
        {
            if (string.IsNullOrEmpty(childColumnNames))
            {
                MessageBox.Show("Cheia 'childColumnNames' lipsește din App.config");
                return;
            }

            string[] columnNames = childColumnNames.Split(',').Select(name => name.Trim()).ToArray();

            tableLayoutPanel1.Controls.Clear();
            tableLayoutPanel1.RowCount = 0;
            tableLayoutPanel1.ColumnCount = 2;
            tableLayoutPanel1.AutoSize = true;
            tableLayoutPanel1.AutoSizeMode = AutoSizeMode.GrowAndShrink;

            textBoxes = new TextBox[columnNames.Length];

            for (int i = 0; i < columnNames.Length; i++)
            {
                string colName = columnNames[i];

                Label label = new Label();
                label.Text = colName;
                label.Anchor = AnchorStyles.Right;
                label.AutoSize = true;

                TextBox textBox = new TextBox();
                textBox.Name = "txt" + colName;
                textBox.Anchor = AnchorStyles.Left | AnchorStyles.Right;
                textBox.Width = 150;
                textBoxes[i] = textBox;

                tableLayoutPanel1.RowStyles.Add(new RowStyle(SizeType.AutoSize));
                tableLayoutPanel1.Controls.Add(label, 0, i); 
                tableLayoutPanel1.Controls.Add(textBox, 1, i); 
                tableLayoutPanel1.RowCount++;
            }
        }


        private void connect_Click(object sender, EventArgs e)
        {
            da.SelectCommand = new SqlCommand("Select * from " + parentName, cs);
            dsParent.Clear();
            da.Fill(dsParent);

            dataGridViewParent.DataSource = dsParent.Tables[0];
            bsParent.DataSource = dsParent.Tables[0];

        }


        private void buttonExit_Click(object sender, EventArgs e)
        {
            DialogResult dialogResult = MessageBox.Show("Are you sure you want to exit?", "Exit Confirmation", MessageBoxButtons.YesNo);
            if (dialogResult == DialogResult.Yes)
            {
                Application.Exit();
            }
        }


        private void dataGridViewParent_CellClick(object sender, DataGridViewCellEventArgs e)
        {
            try
            {
                if (e.RowIndex < 0 || e.RowIndex >= dataGridViewParent.Rows.Count)
                {
                    MessageBox.Show("Invalid row selected!");
                    return;
                }

                if (dataGridViewParent.Rows[e.RowIndex].Cells[0].Value == null ||
                    string.IsNullOrWhiteSpace(dataGridViewParent.Rows[e.RowIndex].Cells[0].Value.ToString()))
                {
                    da.SelectCommand = new SqlCommand("SELECT * FROM " + childName, cs);
                    MessageBox.Show("Displaying all products!");
                }
                else
                {
                    string Cod = dataGridViewParent.Rows[e.RowIndex].Cells[0].Value.ToString();

                    da.SelectCommand = new SqlCommand("SELECT * FROM " + childName + " WHERE " + childName + "." + childToParentID + " = " + Cod, cs);
                    da.SelectCommand.Parameters.AddWithValue("@CodD", Cod);
                }

                dsChild.Clear();
                da.Fill(dsChild);

                if (dsChild.Tables[0].Rows.Count > 0)
                {
                    bsChild.DataSource = dsChild.Tables[0];
                    dataGridViewChild.DataSource = bsChild;

                }
                else
                {
                    MessageBox.Show("No data available!");
                    dataGridViewChild.DataSource = null;
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error: " + ex.Message);
            }
        }

        private void buttonAdd_Click(object sender, EventArgs e)
        {
            if (dataGridViewParent.SelectedRows.Count == 0)
            {
                MessageBox.Show("Please select a row from the department table!");
                return;
            }

            da.InsertCommand = new SqlCommand(insert, cs);
            string f_key = dataGridViewParent.SelectedRows[0].Cells[0].Value.ToString();
            da.InsertCommand.Parameters.Add("@id", SqlDbType.Int).Value = f_key;
            
            string[] args = childArr.Split(',');
            string[] types = childColumnTypes.Split(',');

            try
            {
                for (int i = 0; i < childNumberOfColumns-1; i++)
                {
                    string arg = args[i].Trim(); 
                    string type = types[i].Trim();

                    AddParameterToCommand(da.InsertCommand, arg, type, textBoxes[i].Text);
                }
                
                cs.Open();
                da.InsertCommand.ExecuteNonQuery();
                MessageBox.Show("Added successfully!");

                cs.Close();
                dsChild.Clear();
                da.Fill(dsChild);

                bsChild.DataSource = dsChild.Tables[0];
                dataGridViewChild.DataSource = bsChild;
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error: " + ex.Message);
            }
        }

        private void AddParameterToCommand(SqlCommand command, string paramName, string type, string value)
        {
            // Verifică dacă parametrul există deja în comandă
            if (!command.Parameters.Contains(paramName))
            {
                switch (type.ToLower())
                {
                    case "string":
                        command.Parameters.Add(new SqlParameter(paramName, SqlDbType.VarChar)).Value = value;
                        break;
                    case "int":
                        if (int.TryParse(value, out int intValue))
                        {
                            command.Parameters.Add(new SqlParameter(paramName, SqlDbType.Int)).Value = intValue;
                        }
                        else
                        {
                            MessageBox.Show($"Invalid integer value for {paramName}");
                        }
                        break;
                    default:
                        MessageBox.Show($"Unsupported data type: {type} for parameter {paramName}");
                        break;
                }
            }
            else
            {
                // Actualizează parametrul existent cu valoarea curentă
                command.Parameters[paramName].Value = value;
            }
        }


        private void buttonUpdate_Click(object sender, EventArgs e)
        {
            if (dataGridViewChild.SelectedRows.Count == 0)
            {
                MessageBox.Show("Please select a row from the child table!");
                return;
            }
           
            
            da.UpdateCommand = new SqlCommand(update, cs);

            string p_key = dataGridViewChild.SelectedRows[0].Cells[0].Value.ToString();
            if (!da.UpdateCommand.Parameters.Contains("@id"))
            {
                da.UpdateCommand.Parameters.Add("@id", SqlDbType.Int).Value = p_key;
            }

            string[] args = childArr.Split(',');
            string[] types = childColumnTypes.Split(',');

            try
            {
                for (int i = 0; i < childNumberOfColumns; i++)
                {
                    string arg = args[i].Trim();
                    string type = types[i].Trim();

                    AddParameterToCommand(da.UpdateCommand, arg, type, textBoxes[i].Text);
                }

                cs.Open();
                da.UpdateCommand.ExecuteNonQuery();
                MessageBox.Show("Updated successfully!");

                cs.Close();

                dsChild.Clear();
                da.Fill(dsChild);

                bsChild.DataSource = dsChild.Tables[0];
                dataGridViewChild.DataSource = bsChild;
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error: " + ex.Message);
            }

            

        }

        private void buttonDelete_Click(object sender, EventArgs e)
        {
            if (dataGridViewChild.SelectedRows.Count == 0)
            {
                MessageBox.Show("Please select a row from the child table!");
                return;
            }

            int cod;
            if (dataGridViewChild.SelectedRows[0].Cells[0].Value == null ||
                !int.TryParse(dataGridViewChild.SelectedRows[0].Cells[0].Value.ToString(), out cod))
            {
                MessageBox.Show("Invalid!");
                return;
            }

            DialogResult dialogResult = MessageBox.Show("Are you sure you want to delete this product?", "Delete Confirmation", MessageBoxButtons.YesNo);
            if (dialogResult == DialogResult.No)
            {
                return;
            }

            da.DeleteCommand = new SqlCommand(delete, cs);
            da.DeleteCommand.Parameters.Add("@id", SqlDbType.Int).Value = cod;

            cs.Open();
            da.DeleteCommand.ExecuteNonQuery();
            MessageBox.Show("Deleted successfully!");
            cs.Close();

            dsChild.Clear();
            da.Fill(dsChild);

            dataGridViewChild.ClearSelection();
        }

        private void dataGridViewChildViewUpdate()
        {


            dataGridViewChild.ClearSelection();
            Debug.WriteLine(bsChild.Position);

            if (dataGridViewChild.Rows.Count > 0 && bsChild.Position >= 0 && bsChild.Position < dataGridViewChild.Rows.Count)
            {
                dataGridViewChild.Rows[bsChild.Position].Selected = true;
            }
            else
            {
                MessageBox.Show("No rows available in the child table!");
            }

            records();
        }


        private void records()
        {
            labelRecords.Text = "Record " + (bsChild.Position + 1) + " of " + bsChild.Count;
        }


        private void buttonFirst_Click(object sender, EventArgs e)
        {
            bsChild.MoveFirst();
            dataGridViewChildViewUpdate();
            records();
        }


        private void buttonLast_Click(object sender, EventArgs e)
        {
            bsChild.MoveLast();
            dataGridViewChildViewUpdate();
            records();
        }


        private void buttonPrevious_Click(object sender, EventArgs e)
        {
            bsChild.MovePrevious();
            dataGridViewChildViewUpdate();
            records();
        }


        private void buttonNext_Click(object sender, EventArgs e)
        {
            bsChild.MoveNext();
            dataGridViewChildViewUpdate();
            records();
        }

       
    }
}
