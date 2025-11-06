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

namespace exam
{
    public partial class Form1 : Form
    {
        SqlConnection cs = new SqlConnection("Data Source=LAR_LOQ\\SQLEXPRESS;Initial Catalog=Masini;Integrated Security=True");
        SqlDataAdapter da = new SqlDataAdapter();
        DataSet dsParent = new DataSet();
        DataSet dsChild = new DataSet();
        BindingSource bsParent = new BindingSource();
        BindingSource bsChild = new BindingSource();
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            dataGridViewParent.CellClick += dataGridViewParent_CellClick;
        }

        private void Connect_Click(object sender, EventArgs e)
        {
            da.SelectCommand = new SqlCommand("Select * from Colectie", cs);
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
                    da.SelectCommand = new SqlCommand("SELECT * FROM Masina;", cs);
                    MessageBox.Show("Displaying all Masina!");
                }
                else
                {
                    string CodColectie = cellValue.ToString();
                    da.SelectCommand = new SqlCommand("SELECT * FROM Masina WHERE CodColectie = @CodColectie;", cs);
                    da.SelectCommand.Parameters.Clear();
                    da.SelectCommand.Parameters.AddWithValue("@CodColectie", CodColectie);
                }

                dsChild.Clear();
                da.Fill(dsChild);

                if (dsChild.Tables[0].Rows.Count > 0)
                {
                    bsChild.DataSource = dsChild.Tables[0];
                    dataGridViewChild.DataSource = bsChild;

                    txtMarca.DataBindings.Clear();
                    txtModel.DataBindings.Clear();
                    txtAnFabricatie.DataBindings.Clear();
                    txtValoareEstimata.DataBindings.Clear();
                    txtProprietar.DataBindings.Clear();

                    txtMarca.DataBindings.Add("Text", bsChild, "Marca");
                    txtModel.DataBindings.Add("Text", bsChild, "Model");
                    txtAnFabricatie.DataBindings.Add("Text", bsChild, "AnFabricatie");
                    txtValoareEstimata.DataBindings.Add("Text", bsChild, "ValoareEstimata");
                    txtProprietar.DataBindings.Add("Text", bsChild, "Proprietar");
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
                MessageBox.Show("A row in Colectie must be selected");
                return;
            }

            if (!ValidateInputs(out string marca, out string model, out int anfabricatie, out int valoareestimata, out string proprietar))
            {
                return;
            }


            da.InsertCommand = new SqlCommand("Insert into Masina values (@marca,@model,@anfabricatie,@valoareestimata,@proprietar,@C);", cs);

            da.InsertCommand.Parameters.Add("@C", SqlDbType.Int).Value = dsParent.Tables[dataGridViewParent.CurrentCell.ColumnIndex].Rows[dataGridViewParent.CurrentCell.RowIndex][0];

            da.InsertCommand.Parameters.Add("@marca", SqlDbType.VarChar).Value = marca;
            da.InsertCommand.Parameters.Add("@model", SqlDbType.VarChar).Value = model;
            da.InsertCommand.Parameters.Add("@anfabricatie", SqlDbType.Int).Value = anfabricatie;
            da.InsertCommand.Parameters.Add("@valoareestimata", SqlDbType.Int).Value = valoareestimata;
            da.InsertCommand.Parameters.Add("@proprietar", SqlDbType.VarChar).Value = proprietar;

            cs.Open();
            da.InsertCommand.ExecuteNonQuery();
            MessageBox.Show("Masina added successfully!");
            cs.Close();
            dsChild.Clear();
            da.Fill(dsChild);
        }

        private void Delete_Click(object sender, EventArgs e)
        {
            if (dataGridViewChild.SelectedCells.Count == 0)
            {
                MessageBox.Show("A row in Masina must be selected");
                return;
            }

            DialogResult dialogResult = MessageBox.Show("Are you sure you want to delete this?", "Delete Confirmation", MessageBoxButtons.YesNo);
            if (dialogResult == DialogResult.No)
            {
                return;
            }

            da.DeleteCommand = new SqlCommand("DELETE FROM Masina where CodMasina=@CodMasina", cs);
            da.DeleteCommand.Parameters.Add("@CodMasina", SqlDbType.Int).Value = dsChild.Tables[0].Rows[dataGridViewChild.CurrentCell.RowIndex][0];

            cs.Open();
            da.DeleteCommand.ExecuteNonQuery();
            MessageBox.Show("Masina deleted!");
            cs.Close();

            dsChild.Clear();
            da.Fill(dsChild);
        }

        private void UpdateBtn_Click(object sender, EventArgs e)
        {
            if (dataGridViewChild.SelectedCells.Count == 0)
            {
                MessageBox.Show("A row in Masina must be selected");
                return;
            }

            if (!ValidateInputs(out string marca, out string model, out int anfabricatie, out int valoareestimata, out string proprietar))
            {
                return;
            }

            da.UpdateCommand = new SqlCommand("Update Masina set Marca=@marca, Model=@model, AnFabricatie=@anfabricatie, ValoareEstimata=@valoareestimata,Proprietar=@proprietar where CodMasina=@id", cs);

            da.UpdateCommand.Parameters.Add("@id", SqlDbType.Int).Value = dsChild.Tables[0].Rows[dataGridViewChild.CurrentCell.RowIndex][0];

            da.UpdateCommand.Parameters.Add("@marca", SqlDbType.VarChar).Value = marca;
            da.UpdateCommand.Parameters.Add("@model", SqlDbType.VarChar).Value = model;
            da.UpdateCommand.Parameters.Add("@anfabricatie", SqlDbType.Int).Value = anfabricatie;
            da.UpdateCommand.Parameters.Add("@valoareestimata", SqlDbType.Int).Value = valoareestimata;
            da.UpdateCommand.Parameters.Add("@proprietar", SqlDbType.VarChar).Value = proprietar;

            cs.Open();
            da.UpdateCommand.ExecuteNonQuery();
            MessageBox.Show("Masina updated successfully!");
            cs.Close();
            dsChild.Clear();
            da.Fill(dsChild);
        }

        private bool ValidateInputs(out string marca, out string model, out int anfabricatie, out int valoareestimata, out string proprietar)
        {
            marca = txtMarca.Text.Trim();
            model = txtModel.Text.Trim();
            proprietar = txtProprietar.Text.Trim();
            anfabricatie = 0;
            valoareestimata = 0;

            if (string.IsNullOrWhiteSpace(marca))
            {
                MessageBox.Show("Marca nu poate fi goală!");
                return false;
            }

            if (string.IsNullOrWhiteSpace(model))
            {
                MessageBox.Show("Modelul nu poate fi gol!");
                return false;
            }

            if (!int.TryParse(txtAnFabricatie.Text.Trim(), out anfabricatie))
            {
                MessageBox.Show("Anul fabricației trebuie să fie un număr valid!");
                return false;
            }

            if (!int.TryParse(txtValoareEstimata.Text.Trim(), out valoareestimata))
            {
                MessageBox.Show("Valoarea estimată trebuie să fie un număr valid!");
                return false;
            }

            if (string.IsNullOrWhiteSpace(proprietar))
            {
                MessageBox.Show("Proprietarul nu poate fi gol!");
                return false;
            }

            return true;
        }
    }
}
