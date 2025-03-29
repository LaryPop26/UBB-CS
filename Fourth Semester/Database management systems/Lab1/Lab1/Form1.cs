using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Data.SqlClient;
using System.Diagnostics;

namespace Lab1
{
    public partial class Form1 : Form
    {
        SqlConnection cs = new SqlConnection("Data Source=LAR_LOQ\\SQLEXPRESS;Initial Catalog=VideoGamesStore;Integrated Security=True");
        SqlDataAdapter da = new SqlDataAdapter();
        DataSet dsParent = new DataSet();
        DataSet dsChild = new DataSet();
        BindingSource bsParent = new BindingSource();
        BindingSource bsChild = new BindingSource();
        public Form1()
        {
            InitializeComponent();
        }


        private void connect_Click(object sender, EventArgs e)
        {
            da.SelectCommand = new SqlCommand("Select * from Departament", cs);
            dsParent.Clear();
            da.Fill(dsParent);

            dataGridViewParent.DataSource = dsParent.Tables[0];
            bsParent.DataSource = dsParent.Tables[0];

            comboBoxCodD.Items.Clear();
            foreach (DataRow row in dsParent.Tables[0].Rows)
            {
                comboBoxCodD.Items.Add(row["CodD"].ToString());
            }

            dataGridViewChild.DataSource = null;

        }


        private void buttonExit_Click(object sender, EventArgs e)
        {
            DialogResult dialogResult = MessageBox.Show("Are you sure you want to exit?", "Exit Confirmation", MessageBoxButtons.YesNo);
            if (dialogResult == DialogResult.Yes)
            {
                Application.Exit(); // Închide aplicația
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
                    da.SelectCommand = new SqlCommand("SELECT * FROM Produs;", cs);
                    MessageBox.Show("Displaying all products!");
                }
                else
                {
                    string CodD = dataGridViewParent.Rows[e.RowIndex].Cells[0].Value.ToString();

                    da.SelectCommand = new SqlCommand("SELECT * FROM Produs WHERE CodD = @CodD;", cs);
                    da.SelectCommand.Parameters.AddWithValue("@CodD", CodD);
                }

                dsChild.Clear();
                da.Fill(dsChild);

                if (dsChild.Tables[0].Rows.Count > 0)
                {
                    bsChild.DataSource = dsChild.Tables[0];
                    dataGridViewChild.DataSource = bsChild;

                    txtCodPr.DataBindings.Clear();
                    txtNumePr.DataBindings.Clear();
                    txtPret.DataBindings.Clear();
                    txtCantitate.DataBindings.Clear();
                    comboBoxCodD.DataBindings.Clear();

                    txtCodPr.DataBindings.Add("Text", bsChild, "CodPr");
                    txtNumePr.DataBindings.Add("Text", bsChild, "NumePr");
                    txtPret.DataBindings.Add("Text", bsChild, "Pret");
                    txtCantitate.DataBindings.Add("Text", bsChild, "Cantitate");
                    comboBoxCodD.DataBindings.Add("Text", bsChild, "CodD");
                }
                else
                {
                    MessageBox.Show("No products available for this CodD!");
                    dataGridViewChild.DataSource = null;
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error: " + ex.Message);
            }
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


        private void buttonAdd_Click(object sender, EventArgs e)
        {
            if (dataGridViewParent.SelectedRows.Count == 0)
            {
                MessageBox.Show("Please select a row from the department table!");
                return;
            }

            if (dataGridViewParent.SelectedRows[0].Cells[0].Value == null)
            {
                MessageBox.Show("Invalid CodD!");
                return;
            }


            int codPr;
            if (!int.TryParse(txtCodPr.Text, out codPr))
            {
                MessageBox.Show("CodPr must be a valid integer!");
                return;
            }

            int codD;
            if (!int.TryParse(comboBoxCodD.Text, out codD) || codD < 0)
            {
                MessageBox.Show("CodD must be a positive integer!");
                return;
            }


            string numePr = txtNumePr.Text.Trim();
            if (string.IsNullOrWhiteSpace(numePr))
            {
                MessageBox.Show("Product name cannot be empty!");
                return;
            }

            int pret;
            if (!int.TryParse(txtPret.Text, out pret) || pret <= 0)
            {
                MessageBox.Show("Price must be a positive integer!");
                return;
            }

            int cantitate;
            if (!int.TryParse(txtCantitate.Text, out cantitate) || cantitate < 0)
            {
                MessageBox.Show("Quantity must be a positive integer!");
                return;
            }

            int exists = 0;
            SqlCommand checkCmd = new SqlCommand("SELECT COUNT(*) FROM Produs WHERE CodPr = @codPr", cs);
            checkCmd.Parameters.AddWithValue("@codPr", codPr);

            try
            {
                cs.Open();
                exists = (int)checkCmd.ExecuteScalar();
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error checking CodPr: " + ex.Message);
                return;
            }
            finally
            {
                if (cs.State == ConnectionState.Open)
                    cs.Close();
            }

            if (exists > 0)
            {
                MessageBox.Show("CodPr already exists! Please enter a unique code.");
                return;
            }

            da.InsertCommand = new SqlCommand("INSERT INTO Produs(CodPr, NumePr, Pret, Cantitate, CodD) VALUES (@codPr, @nume, @pret, @cant, @codD);", cs);

            da.InsertCommand.Parameters.Add("@codPr", SqlDbType.Int).Value = codPr;
            da.InsertCommand.Parameters.Add("@nume", SqlDbType.VarChar).Value = numePr;
            da.InsertCommand.Parameters.Add("@pret", SqlDbType.Int).Value = pret;
            da.InsertCommand.Parameters.Add("@cant", SqlDbType.Int).Value = cantitate;
            da.InsertCommand.Parameters.Add("@codD", SqlDbType.Int).Value = dsParent.Tables[0].Rows[dataGridViewParent.CurrentCell.RowIndex][0];

            cs.Open();
            da.InsertCommand.ExecuteNonQuery();
            MessageBox.Show("Product added successfully!");

            cs.Close();

            dsChild.Clear();
            da.Fill(dsChild);

        }


        private void buttonUpdate_Click(object sender, EventArgs e)
        {
            if (dataGridViewChild.SelectedRows.Count == 0)
            {
                MessageBox.Show("Please select a row from the child table!");
                return;
            }

            string numePr = txtNumePr.Text.Trim();
            if (string.IsNullOrWhiteSpace(numePr))
            {
                MessageBox.Show("Product name cannot be empty!");
                return;
            }

            int pret;
            if (!int.TryParse(txtPret.Text, out pret) || pret <= 0)
            {
                MessageBox.Show("Price must be a positive integer!");
                return;
            }

            int cantitate;
            if (!int.TryParse(txtCantitate.Text, out cantitate) || cantitate < 0)
            {
                MessageBox.Show("Quantity must be a positive integer!");
                return;
            }
            
            da.UpdateCommand = new SqlCommand("UPDATE Produs set NumePr = @nume, pret = @pret, cantitate = @cant, CodD = @codD where codPr = @codPr", cs);
            da.UpdateCommand.Parameters.Add("@codPr", SqlDbType.Int).Value = dsChild.Tables[0].Rows[dataGridViewChild.CurrentCell.RowIndex][0];
            da.UpdateCommand.Parameters.Add("@nume", SqlDbType.VarChar).Value = numePr;
            da.UpdateCommand.Parameters.Add("@pret", SqlDbType.Int).Value = pret;
            da.UpdateCommand.Parameters.Add("@cant", SqlDbType.Int).Value = cantitate;
            da.UpdateCommand.Parameters.Add("@codD", SqlDbType.Int).Value = int.Parse(comboBoxCodD.SelectedItem.ToString());

            cs.Open();
            da.UpdateCommand.ExecuteNonQuery();
            MessageBox.Show("Product updated successfully!");

            cs.Close();

            dsChild.Clear();
            da.Fill(dsChild);

        }

        private void buttonDelete_Click(object sender, EventArgs e)
        {
            if (dataGridViewChild.SelectedRows.Count == 0)
            {
                MessageBox.Show("Please select a row from the child table!");
                return;
            }

            int codPr;
            if (dataGridViewChild.SelectedRows[0].Cells["CodPr"].Value == null ||
                !int.TryParse(dataGridViewChild.SelectedRows[0].Cells["CodPr"].Value.ToString(), out codPr))
            {
                MessageBox.Show("Invalid CodPr!");
                return;
            }

            DialogResult dialogResult = MessageBox.Show("Are you sure you want to delete this product?", "Delete Confirmation", MessageBoxButtons.YesNo);
            if (dialogResult == DialogResult.No)
            {
                return;
            }

            da.DeleteCommand = new SqlCommand("DELETE FROM Produs WHERE CodPr = @codPr;", cs);
            da.DeleteCommand.Parameters.Add("@codPr", SqlDbType.Int).Value = codPr;

            cs.Open();
            da.DeleteCommand.ExecuteNonQuery();
            MessageBox.Show("Product deleted successfully!");
            cs.Close();

            dsChild.Clear();
            da.Fill(dsChild);

            dataGridViewChild.ClearSelection();
        }
    }
}
