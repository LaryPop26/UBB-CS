namespace exam
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.dataGridViewParent = new System.Windows.Forms.DataGridView();
            this.dataGridViewChild = new System.Windows.Forms.DataGridView();
            this.Connect = new System.Windows.Forms.Button();
            this.buttonAdd = new System.Windows.Forms.Button();
            this.Delete = new System.Windows.Forms.Button();
            this.UpdateBtn = new System.Windows.Forms.Button();
            this.Marca = new System.Windows.Forms.Label();
            this.Model = new System.Windows.Forms.Label();
            this.AnFabricatie = new System.Windows.Forms.Label();
            this.ValoareEstimata = new System.Windows.Forms.Label();
            this.Proprietar = new System.Windows.Forms.Label();
            this.txtMarca = new System.Windows.Forms.TextBox();
            this.txtModel = new System.Windows.Forms.TextBox();
            this.txtAnFabricatie = new System.Windows.Forms.TextBox();
            this.txtValoareEstimata = new System.Windows.Forms.TextBox();
            this.txtProprietar = new System.Windows.Forms.TextBox();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridViewParent)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridViewChild)).BeginInit();
            this.SuspendLayout();
            // 
            // dataGridViewParent
            // 
            this.dataGridViewParent.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridViewParent.Location = new System.Drawing.Point(29, 35);
            this.dataGridViewParent.Name = "dataGridViewParent";
            this.dataGridViewParent.RowHeadersWidth = 51;
            this.dataGridViewParent.RowTemplate.Height = 24;
            this.dataGridViewParent.Size = new System.Drawing.Size(485, 174);
            this.dataGridViewParent.TabIndex = 0;
            // 
            // dataGridViewChild
            // 
            this.dataGridViewChild.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridViewChild.Location = new System.Drawing.Point(29, 239);
            this.dataGridViewChild.Name = "dataGridViewChild";
            this.dataGridViewChild.RowHeadersWidth = 51;
            this.dataGridViewChild.RowTemplate.Height = 24;
            this.dataGridViewChild.Size = new System.Drawing.Size(986, 173);
            this.dataGridViewChild.TabIndex = 1;
            // 
            // Connect
            // 
            this.Connect.Location = new System.Drawing.Point(893, 29);
            this.Connect.Name = "Connect";
            this.Connect.Size = new System.Drawing.Size(80, 34);
            this.Connect.TabIndex = 2;
            this.Connect.Text = "Connect";
            this.Connect.UseVisualStyleBackColor = true;
            this.Connect.Click += new System.EventHandler(this.Connect_Click);
            // 
            // buttonAdd
            // 
            this.buttonAdd.Location = new System.Drawing.Point(893, 74);
            this.buttonAdd.Name = "buttonAdd";
            this.buttonAdd.Size = new System.Drawing.Size(80, 34);
            this.buttonAdd.TabIndex = 3;
            this.buttonAdd.Text = "Add";
            this.buttonAdd.UseVisualStyleBackColor = true;
            this.buttonAdd.Click += new System.EventHandler(this.buttonAdd_Click);
            // 
            // Delete
            // 
            this.Delete.Location = new System.Drawing.Point(893, 134);
            this.Delete.Name = "Delete";
            this.Delete.Size = new System.Drawing.Size(80, 34);
            this.Delete.TabIndex = 4;
            this.Delete.Text = "Delete";
            this.Delete.UseVisualStyleBackColor = true;
            this.Delete.Click += new System.EventHandler(this.Delete_Click);
            // 
            // UpdateBtn
            // 
            this.UpdateBtn.Location = new System.Drawing.Point(893, 178);
            this.UpdateBtn.Name = "UpdateBtn";
            this.UpdateBtn.Size = new System.Drawing.Size(80, 34);
            this.UpdateBtn.TabIndex = 5;
            this.UpdateBtn.Text = "Update";
            this.UpdateBtn.UseVisualStyleBackColor = true;
            this.UpdateBtn.Click += new System.EventHandler(this.UpdateBtn_Click);
            // 
            // Marca
            // 
            this.Marca.AutoSize = true;
            this.Marca.Location = new System.Drawing.Point(551, 38);
            this.Marca.Name = "Marca";
            this.Marca.Size = new System.Drawing.Size(45, 16);
            this.Marca.TabIndex = 7;
            this.Marca.Text = "Marca";
            // 
            // Model
            // 
            this.Model.AutoSize = true;
            this.Model.Location = new System.Drawing.Point(551, 74);
            this.Model.Name = "Model";
            this.Model.Size = new System.Drawing.Size(45, 16);
            this.Model.TabIndex = 8;
            this.Model.Text = "Model";
            // 
            // AnFabricatie
            // 
            this.AnFabricatie.AutoSize = true;
            this.AnFabricatie.Location = new System.Drawing.Point(551, 114);
            this.AnFabricatie.Name = "AnFabricatie";
            this.AnFabricatie.Size = new System.Drawing.Size(83, 16);
            this.AnFabricatie.TabIndex = 9;
            this.AnFabricatie.Text = "AnFabricatie";
            // 
            // ValoareEstimata
            // 
            this.ValoareEstimata.AutoSize = true;
            this.ValoareEstimata.Location = new System.Drawing.Point(551, 152);
            this.ValoareEstimata.Name = "ValoareEstimata";
            this.ValoareEstimata.Size = new System.Drawing.Size(107, 16);
            this.ValoareEstimata.TabIndex = 10;
            this.ValoareEstimata.Text = "ValoareEstimata";
            // 
            // Proprietar
            // 
            this.Proprietar.AutoSize = true;
            this.Proprietar.Location = new System.Drawing.Point(551, 187);
            this.Proprietar.Name = "Proprietar";
            this.Proprietar.Size = new System.Drawing.Size(66, 16);
            this.Proprietar.TabIndex = 11;
            this.Proprietar.Text = "Proprietar";
            // 
            // txtMarca
            // 
            this.txtMarca.Location = new System.Drawing.Point(688, 35);
            this.txtMarca.Name = "txtMarca";
            this.txtMarca.Size = new System.Drawing.Size(125, 22);
            this.txtMarca.TabIndex = 12;
            // 
            // txtModel
            // 
            this.txtModel.Location = new System.Drawing.Point(688, 71);
            this.txtModel.Name = "txtModel";
            this.txtModel.Size = new System.Drawing.Size(125, 22);
            this.txtModel.TabIndex = 13;
            // 
            // txtAnFabricatie
            // 
            this.txtAnFabricatie.Location = new System.Drawing.Point(688, 111);
            this.txtAnFabricatie.Name = "txtAnFabricatie";
            this.txtAnFabricatie.Size = new System.Drawing.Size(125, 22);
            this.txtAnFabricatie.TabIndex = 14;
            // 
            // txtValoareEstimata
            // 
            this.txtValoareEstimata.Location = new System.Drawing.Point(688, 146);
            this.txtValoareEstimata.Name = "txtValoareEstimata";
            this.txtValoareEstimata.Size = new System.Drawing.Size(125, 22);
            this.txtValoareEstimata.TabIndex = 15;
            // 
            // txtProprietar
            // 
            this.txtProprietar.Location = new System.Drawing.Point(688, 187);
            this.txtProprietar.Name = "txtProprietar";
            this.txtProprietar.Size = new System.Drawing.Size(125, 22);
            this.txtProprietar.TabIndex = 16;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1047, 435);
            this.Controls.Add(this.txtProprietar);
            this.Controls.Add(this.txtValoareEstimata);
            this.Controls.Add(this.txtAnFabricatie);
            this.Controls.Add(this.txtModel);
            this.Controls.Add(this.txtMarca);
            this.Controls.Add(this.Proprietar);
            this.Controls.Add(this.ValoareEstimata);
            this.Controls.Add(this.AnFabricatie);
            this.Controls.Add(this.Model);
            this.Controls.Add(this.Marca);
            this.Controls.Add(this.UpdateBtn);
            this.Controls.Add(this.Delete);
            this.Controls.Add(this.buttonAdd);
            this.Controls.Add(this.Connect);
            this.Controls.Add(this.dataGridViewChild);
            this.Controls.Add(this.dataGridViewParent);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.dataGridViewParent)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridViewChild)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.DataGridView dataGridViewParent;
        private System.Windows.Forms.DataGridView dataGridViewChild;
        private System.Windows.Forms.Button Connect;
        private System.Windows.Forms.Button buttonAdd;
        private System.Windows.Forms.Button Delete;
        private System.Windows.Forms.Button UpdateBtn;
        private System.Windows.Forms.Label Marca;
        private System.Windows.Forms.Label Model;
        private System.Windows.Forms.Label AnFabricatie;
        private System.Windows.Forms.Label ValoareEstimata;
        private System.Windows.Forms.Label Proprietar;
        private System.Windows.Forms.TextBox txtMarca;
        private System.Windows.Forms.TextBox txtModel;
        private System.Windows.Forms.TextBox txtAnFabricatie;
        private System.Windows.Forms.TextBox txtValoareEstimata;
        private System.Windows.Forms.TextBox txtProprietar;
    }
}

