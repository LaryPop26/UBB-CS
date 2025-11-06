namespace S5_exemplu
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
            this.Connect = new System.Windows.Forms.Button();
            this.buttonAdd = new System.Windows.Forms.Button();
            this.Delete = new System.Windows.Forms.Button();
            this.UpdateBtn = new System.Windows.Forms.Button();
            this.dataGridViewParent = new System.Windows.Forms.DataGridView();
            this.dataGridViewChild = new System.Windows.Forms.DataGridView();
            this.txtNume = new System.Windows.Forms.TextBox();
            this.txtPrenume = new System.Windows.Forms.TextBox();
            this.txtTitulatura = new System.Windows.Forms.TextBox();
            this.txtGen = new System.Windows.Forms.TextBox();
            this.Nume = new System.Windows.Forms.Label();
            this.Prenume = new System.Windows.Forms.Label();
            this.Titulatura = new System.Windows.Forms.Label();
            this.Gen = new System.Windows.Forms.Label();
            this.DataNastere = new System.Windows.Forms.Label();
            this.txtDataNastere = new System.Windows.Forms.TextBox();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridViewParent)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridViewChild)).BeginInit();
            this.SuspendLayout();
            // 
            // Connect
            // 
            this.Connect.Location = new System.Drawing.Point(28, 27);
            this.Connect.Name = "Connect";
            this.Connect.Size = new System.Drawing.Size(87, 30);
            this.Connect.TabIndex = 0;
            this.Connect.Text = "Connect";
            this.Connect.UseVisualStyleBackColor = true;
            this.Connect.Click += new System.EventHandler(this.Connect_Click);
            // 
            // buttonAdd
            // 
            this.buttonAdd.Location = new System.Drawing.Point(228, 27);
            this.buttonAdd.Name = "buttonAdd";
            this.buttonAdd.Size = new System.Drawing.Size(87, 30);
            this.buttonAdd.TabIndex = 1;
            this.buttonAdd.Text = "Add";
            this.buttonAdd.UseVisualStyleBackColor = true;
            this.buttonAdd.Click += new System.EventHandler(this.buttonAdd_Click);
            // 
            // Delete
            // 
            this.Delete.Location = new System.Drawing.Point(343, 27);
            this.Delete.Name = "Delete";
            this.Delete.Size = new System.Drawing.Size(87, 30);
            this.Delete.TabIndex = 2;
            this.Delete.Text = "Delete";
            this.Delete.UseVisualStyleBackColor = true;
            this.Delete.Click += new System.EventHandler(this.Delete_Click);
            // 
            // UpdateBtn
            // 
            this.UpdateBtn.Location = new System.Drawing.Point(457, 27);
            this.UpdateBtn.Name = "UpdateBtn";
            this.UpdateBtn.Size = new System.Drawing.Size(87, 30);
            this.UpdateBtn.TabIndex = 3;
            this.UpdateBtn.Text = "Update";
            this.UpdateBtn.UseVisualStyleBackColor = true;
            this.UpdateBtn.Click += new System.EventHandler(this.UpdateBtn_Click);
            // 
            // dataGridViewParent
            // 
            this.dataGridViewParent.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridViewParent.Location = new System.Drawing.Point(28, 75);
            this.dataGridViewParent.Name = "dataGridViewParent";
            this.dataGridViewParent.RowHeadersWidth = 51;
            this.dataGridViewParent.RowTemplate.Height = 24;
            this.dataGridViewParent.Size = new System.Drawing.Size(572, 186);
            this.dataGridViewParent.TabIndex = 4;
            this.dataGridViewParent.CellClick += new System.Windows.Forms.DataGridViewCellEventHandler(this.dataGridViewParent_CellClick);
            // 
            // dataGridViewChild
            // 
            this.dataGridViewChild.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridViewChild.Location = new System.Drawing.Point(28, 278);
            this.dataGridViewChild.Name = "dataGridViewChild";
            this.dataGridViewChild.RowHeadersWidth = 51;
            this.dataGridViewChild.RowTemplate.Height = 24;
            this.dataGridViewChild.Size = new System.Drawing.Size(572, 181);
            this.dataGridViewChild.TabIndex = 5;
            // 
            // txtNume
            // 
            this.txtNume.Location = new System.Drawing.Point(727, 103);
            this.txtNume.Name = "txtNume";
            this.txtNume.Size = new System.Drawing.Size(100, 22);
            this.txtNume.TabIndex = 6;
            // 
            // txtPrenume
            // 
            this.txtPrenume.Location = new System.Drawing.Point(727, 168);
            this.txtPrenume.Name = "txtPrenume";
            this.txtPrenume.Size = new System.Drawing.Size(100, 22);
            this.txtPrenume.TabIndex = 7;
            // 
            // txtTitulatura
            // 
            this.txtTitulatura.Location = new System.Drawing.Point(727, 239);
            this.txtTitulatura.Name = "txtTitulatura";
            this.txtTitulatura.Size = new System.Drawing.Size(100, 22);
            this.txtTitulatura.TabIndex = 8;
            // 
            // txtGen
            // 
            this.txtGen.Location = new System.Drawing.Point(727, 297);
            this.txtGen.Name = "txtGen";
            this.txtGen.Size = new System.Drawing.Size(100, 22);
            this.txtGen.TabIndex = 9;
            // 
            // Nume
            // 
            this.Nume.AutoSize = true;
            this.Nume.Location = new System.Drawing.Point(633, 109);
            this.Nume.Name = "Nume";
            this.Nume.Size = new System.Drawing.Size(43, 16);
            this.Nume.TabIndex = 10;
            this.Nume.Text = "Nume";
            // 
            // Prenume
            // 
            this.Prenume.AutoSize = true;
            this.Prenume.Location = new System.Drawing.Point(633, 171);
            this.Prenume.Name = "Prenume";
            this.Prenume.Size = new System.Drawing.Size(61, 16);
            this.Prenume.TabIndex = 11;
            this.Prenume.Text = "Prenume";
            // 
            // Titulatura
            // 
            this.Titulatura.AutoSize = true;
            this.Titulatura.Location = new System.Drawing.Point(633, 245);
            this.Titulatura.Name = "Titulatura";
            this.Titulatura.Size = new System.Drawing.Size(62, 16);
            this.Titulatura.TabIndex = 12;
            this.Titulatura.Text = "Titulatura";
            // 
            // Gen
            // 
            this.Gen.AutoSize = true;
            this.Gen.Location = new System.Drawing.Point(633, 303);
            this.Gen.Name = "Gen";
            this.Gen.Size = new System.Drawing.Size(32, 16);
            this.Gen.TabIndex = 13;
            this.Gen.Text = "Gen";
            // 
            // DataNastere
            // 
            this.DataNastere.AutoSize = true;
            this.DataNastere.Location = new System.Drawing.Point(633, 368);
            this.DataNastere.Name = "DataNastere";
            this.DataNastere.Size = new System.Drawing.Size(84, 16);
            this.DataNastere.TabIndex = 14;
            this.DataNastere.Text = "DataNastere";
            // 
            // txtDataNastere
            // 
            this.txtDataNastere.Location = new System.Drawing.Point(727, 362);
            this.txtDataNastere.Name = "txtDataNastere";
            this.txtDataNastere.Size = new System.Drawing.Size(100, 22);
            this.txtDataNastere.TabIndex = 15;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(891, 484);
            this.Controls.Add(this.txtDataNastere);
            this.Controls.Add(this.DataNastere);
            this.Controls.Add(this.Gen);
            this.Controls.Add(this.Titulatura);
            this.Controls.Add(this.Prenume);
            this.Controls.Add(this.Nume);
            this.Controls.Add(this.txtGen);
            this.Controls.Add(this.txtTitulatura);
            this.Controls.Add(this.txtPrenume);
            this.Controls.Add(this.txtNume);
            this.Controls.Add(this.dataGridViewChild);
            this.Controls.Add(this.dataGridViewParent);
            this.Controls.Add(this.UpdateBtn);
            this.Controls.Add(this.Delete);
            this.Controls.Add(this.buttonAdd);
            this.Controls.Add(this.Connect);
            this.Name = "Form1";
            this.Text = "Form1";
            ((System.ComponentModel.ISupportInitialize)(this.dataGridViewParent)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridViewChild)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button Connect;
        private System.Windows.Forms.Button buttonAdd;
        private System.Windows.Forms.Button Delete;
        private System.Windows.Forms.Button UpdateBtn;
        private System.Windows.Forms.DataGridView dataGridViewParent;
        private System.Windows.Forms.DataGridView dataGridViewChild;
        private System.Windows.Forms.TextBox txtNume;
        private System.Windows.Forms.TextBox txtPrenume;
        private System.Windows.Forms.TextBox txtTitulatura;
        private System.Windows.Forms.TextBox txtGen;
        private System.Windows.Forms.Label Nume;
        private System.Windows.Forms.Label Prenume;
        private System.Windows.Forms.Label Titulatura;
        private System.Windows.Forms.Label Gen;
        private System.Windows.Forms.Label DataNastere;
        private System.Windows.Forms.TextBox txtDataNastere;
    }
}

