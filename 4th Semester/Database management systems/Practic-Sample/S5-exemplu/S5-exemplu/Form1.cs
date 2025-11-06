using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Data.SqlClient;
using System.Drawing;
using System.Globalization;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace S5_exemplu
{
    public partial class Form1: Form
    {
        SqlConnection cs = new SqlConnection("Data Source=LAR_LOQ\\SQLEXPRESS;Initial Catalog=S5;Integrated Security=True");
        SqlDataAdapter da = new SqlDataAdapter();
        DataSet dsParent = new DataSet();
        DataSet dsChild = new DataSet();
        BindingSource bsParent = new BindingSource();
        BindingSource bsChild = new BindingSource();
        public Form1()
        {
            InitializeComponent();
        }

        private void Connect_Click(object sender, EventArgs e)
        {
            da.SelectCommand = new SqlCommand("Select * from Facultati", cs);
            dsParent.Clear();
            da.Fill(dsParent);

            dataGridViewParent.DataSource = dsParent.Tables[0];
            bsParent.DataSource = dsParent.Tables[0];

            dataGridViewChild.DataSource = null;
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

                var cellValue = dataGridViewParent.Rows[e.RowIndex].Cells[0].Value;

                if (cellValue == null || string.IsNullOrWhiteSpace(cellValue.ToString()))
                {
                    da.SelectCommand = new SqlCommand("SELECT * FROM Profesori;", cs);
                    MessageBox.Show("Displaying all Profesori!");
                }
                else
                {
                    string Fid = cellValue.ToString();
                    da.SelectCommand = new SqlCommand("SELECT * FROM Profesori WHERE Fid = @Fid;", cs);
                    da.SelectCommand.Parameters.Clear();
                    da.SelectCommand.Parameters.AddWithValue("@Fid", Fid);
                }

                dsChild.Clear();
                da.Fill(dsChild);

                if (dsChild.Tables[0].Rows.Count > 0)
                {
                    bsChild.DataSource = dsChild.Tables[0];
                    dataGridViewChild.DataSource = bsChild;

                    txtNume.DataBindings.Clear();
                    txtPrenume.DataBindings.Clear();
                    txtTitulatura.DataBindings.Clear();
                    txtGen.DataBindings.Clear();
                    txtDataNastere.DataBindings.Clear();

                    txtNume.DataBindings.Add("Text", bsChild, "Nume");
                    txtPrenume.DataBindings.Add("Text", bsChild, "Prenume");
                    txtTitulatura.DataBindings.Add("Text", bsChild, "Titulatura");
                    txtGen.DataBindings.Add("Text", bsChild, "Gen");
                    txtDataNastere.DataBindings.Add("Text", bsChild, "DataNastere");
                }
                else
                {
                    dataGridViewChild.DataSource = null;
                    MessageBox.Show("No professors for this faculty!");
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error loading Profesori: " + ex.Message);
            }
        }

        private void buttonAdd_Click(object sender, EventArgs e)
        {
            if (dataGridViewParent.SelectedCells.Count == 0)
            {
                MessageBox.Show("A row in Facultati must be selected");
                return;
            }

            if (!ValidateInputs(out string nume, out string prenume, out string titulatura, out string gen, out DateTime dataNastere))
            {
                return;
            }


            da.InsertCommand = new SqlCommand("Insert into Profesori values (@nume,@prenume,@titulatura,@gen,@dataN,@F);", cs);

            da.InsertCommand.Parameters.Add("@F", SqlDbType.Int).Value = dsParent.Tables[dataGridViewParent.CurrentCell.ColumnIndex].Rows[dataGridViewParent.CurrentCell.RowIndex][0];

            da.InsertCommand.Parameters.Add("@nume", SqlDbType.VarChar).Value = nume;
            da.InsertCommand.Parameters.Add("@prenume", SqlDbType.VarChar).Value = prenume;
            da.InsertCommand.Parameters.Add("@titulatura", SqlDbType.VarChar).Value = titulatura;
            da.InsertCommand.Parameters.Add("@gen", SqlDbType.VarChar).Value = gen;
            da.InsertCommand.Parameters.Add("@dataN", SqlDbType.Date).Value = dataNastere;

            cs.Open();
            da.InsertCommand.ExecuteNonQuery();
            MessageBox.Show("Profesor added successfully!");
            cs.Close();
            dsChild.Clear();
            da.Fill(dsChild);
        }

        private void Delete_Click(object sender, EventArgs e)
        {
            if (dataGridViewChild.SelectedCells.Count == 0)
            {
                MessageBox.Show("A row in Profesori must be selected");
                return;
            }

            DialogResult dialogResult = MessageBox.Show("Are you sure you want to delete this?", "Delete Confirmation", MessageBoxButtons.YesNo);
            if (dialogResult == DialogResult.No)
            {
                return;
            }

            da.DeleteCommand = new SqlCommand("DELETE FROM Profesori where Pid=@id", cs);
            da.DeleteCommand.Parameters.Add("@id", SqlDbType.Int).Value = dsChild.Tables[0].Rows[dataGridViewChild.CurrentCell.RowIndex][0];

            cs.Open();
            da.DeleteCommand.ExecuteNonQuery();
            MessageBox.Show("Profesor deleted!");
            cs.Close();

            dsChild.Clear();
            da.Fill(dsChild);
        }

        private void UpdateBtn_Click(object sender, EventArgs e)
        {
            if (dataGridViewChild.SelectedCells.Count == 0)
            {
                MessageBox.Show("A row in Profesori must be selected");
                return;
            }

            if (!ValidateInputs(out string nume, out string prenume, out string titulatura, out string gen, out DateTime dataNastere))
            {
                return;
            }

            da.UpdateCommand = new SqlCommand("Update Profesori set Nume=@nume, Prenume=@prenume, Titulatura=@titulatura, Gen=@gen,DataNastere=@dataN where Pid=@id", cs);

            da.UpdateCommand.Parameters.Add("@id", SqlDbType.Int).Value = dsChild.Tables[0].Rows[dataGridViewChild.CurrentCell.RowIndex][0];

            da.UpdateCommand.Parameters.Add("@nume", SqlDbType.VarChar).Value = nume;
            da.UpdateCommand.Parameters.Add("@prenume", SqlDbType.VarChar).Value = prenume;
            da.UpdateCommand.Parameters.Add("@titulatura", SqlDbType.VarChar).Value = titulatura;
            da.UpdateCommand.Parameters.Add("@gen", SqlDbType.VarChar).Value = gen;
            da.UpdateCommand.Parameters.Add("@dataN", SqlDbType.Date).Value = dataNastere;

            cs.Open();
            da.UpdateCommand.ExecuteNonQuery();
            MessageBox.Show("Profesor updated successfully!");
            cs.Close();
            dsChild.Clear();
            da.Fill(dsChild);
        }

        private bool ValidateInputs(out string nume, out string prenume, out string titulatura, out string gen, out DateTime dataNastere)
        {
            nume = txtNume.Text.Trim();
            if (string.IsNullOrWhiteSpace(nume))
            {
                MessageBox.Show("Nume cannot be empty!");
                dataNastere = default;
                prenume = titulatura = gen = null;
                return false;
            }

            prenume = txtPrenume.Text.Trim();
            if (string.IsNullOrWhiteSpace(prenume))
            {
                MessageBox.Show("Prenume cannot be empty!");
                dataNastere = default;
                titulatura = gen = null;
                return false;
            }

            titulatura = txtTitulatura.Text.Trim();
            if (string.IsNullOrWhiteSpace(titulatura))
            {
                MessageBox.Show("Titulatura cannot be empty!");
                dataNastere = default;
                gen = null;
                return false;
            }

            gen = txtGen.Text.Trim();
            if (string.IsNullOrWhiteSpace(gen))
            {
                MessageBox.Show("Gen cannot be empty!");
                dataNastere = default;
                return false;
            }

            string format = "dd/mm/yyyy"; // Formatul pe care îl aștepți
            if (!DateTime.TryParseExact(txtDataNastere.Text.Trim(), format, CultureInfo.InvariantCulture, DateTimeStyles.None, out dataNastere))
            {
                MessageBox.Show("Data nașterii nu este într-un format valid (ex: 01/01/2000)!");
                return false;
            }

            return true;
        }

    }
}
