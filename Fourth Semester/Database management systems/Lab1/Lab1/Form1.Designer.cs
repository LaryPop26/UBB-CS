﻿namespace Lab1
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
            this.connect = new System.Windows.Forms.Button();
            this.dataGridViewParent = new System.Windows.Forms.DataGridView();
            this.dataGridViewChild = new System.Windows.Forms.DataGridView();
            this.buttonAdd = new System.Windows.Forms.Button();
            this.buttonUpdate = new System.Windows.Forms.Button();
            this.buttonDelete = new System.Windows.Forms.Button();
            this.txtNumePr = new System.Windows.Forms.TextBox();
            this.txtCantitate = new System.Windows.Forms.TextBox();
            this.txtPret = new System.Windows.Forms.TextBox();
            this.numepr = new System.Windows.Forms.Label();
            this.pret = new System.Windows.Forms.Label();
            this.cantitate = new System.Windows.Forms.Label();
            this.codD = new System.Windows.Forms.Label();
            this.buttonFirst = new System.Windows.Forms.Button();
            this.buttonLast = new System.Windows.Forms.Button();
            this.buttonPrevious = new System.Windows.Forms.Button();
            this.buttonNext = new System.Windows.Forms.Button();
            this.labelRecords = new System.Windows.Forms.Label();
            this.txtCodPr = new System.Windows.Forms.TextBox();
            this.codpr = new System.Windows.Forms.Label();
            this.comboBoxCodD = new System.Windows.Forms.ComboBox();
            this.buttonExit = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridViewParent)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridViewChild)).BeginInit();
            this.SuspendLayout();
            // 
            // connect
            // 
            this.connect.Location = new System.Drawing.Point(11, 27);
            this.connect.Margin = new System.Windows.Forms.Padding(2);
            this.connect.Name = "connect";
            this.connect.Size = new System.Drawing.Size(74, 24);
            this.connect.TabIndex = 0;
            this.connect.Text = "Connect";
            this.connect.UseVisualStyleBackColor = true;
            this.connect.Click += new System.EventHandler(this.connect_Click);
            // 
            // dataGridViewParent
            // 
            this.dataGridViewParent.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridViewParent.Location = new System.Drawing.Point(9, 72);
            this.dataGridViewParent.Margin = new System.Windows.Forms.Padding(2);
            this.dataGridViewParent.Name = "dataGridViewParent";
            this.dataGridViewParent.RowHeadersWidth = 51;
            this.dataGridViewParent.RowTemplate.Height = 24;
            this.dataGridViewParent.Size = new System.Drawing.Size(456, 132);
            this.dataGridViewParent.TabIndex = 1;
            this.dataGridViewParent.CellClick += new System.Windows.Forms.DataGridViewCellEventHandler(this.dataGridViewParent_CellClick);
            // 
            // dataGridViewChild
            // 
            this.dataGridViewChild.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridViewChild.Location = new System.Drawing.Point(9, 220);
            this.dataGridViewChild.Margin = new System.Windows.Forms.Padding(2);
            this.dataGridViewChild.Name = "dataGridViewChild";
            this.dataGridViewChild.RowHeadersWidth = 51;
            this.dataGridViewChild.RowTemplate.Height = 24;
            this.dataGridViewChild.Size = new System.Drawing.Size(456, 297);
            this.dataGridViewChild.TabIndex = 2;
            // 
            // buttonAdd
            // 
            this.buttonAdd.Location = new System.Drawing.Point(490, 72);
            this.buttonAdd.Margin = new System.Windows.Forms.Padding(2);
            this.buttonAdd.Name = "buttonAdd";
            this.buttonAdd.Size = new System.Drawing.Size(74, 24);
            this.buttonAdd.TabIndex = 3;
            this.buttonAdd.Text = "Add";
            this.buttonAdd.UseVisualStyleBackColor = true;
            this.buttonAdd.Click += new System.EventHandler(this.buttonAdd_Click);
            // 
            // buttonUpdate
            // 
            this.buttonUpdate.Location = new System.Drawing.Point(490, 127);
            this.buttonUpdate.Margin = new System.Windows.Forms.Padding(2);
            this.buttonUpdate.Name = "buttonUpdate";
            this.buttonUpdate.Size = new System.Drawing.Size(74, 24);
            this.buttonUpdate.TabIndex = 4;
            this.buttonUpdate.Text = "Update";
            this.buttonUpdate.UseVisualStyleBackColor = true;
            this.buttonUpdate.Click += new System.EventHandler(this.buttonUpdate_Click);
            // 
            // buttonDelete
            // 
            this.buttonDelete.Location = new System.Drawing.Point(490, 180);
            this.buttonDelete.Margin = new System.Windows.Forms.Padding(2);
            this.buttonDelete.Name = "buttonDelete";
            this.buttonDelete.Size = new System.Drawing.Size(74, 24);
            this.buttonDelete.TabIndex = 5;
            this.buttonDelete.Text = "Delete";
            this.buttonDelete.UseVisualStyleBackColor = true;
            this.buttonDelete.Click += new System.EventHandler(this.buttonDelete_Click);
            // 
            // txtNumePr
            // 
            this.txtNumePr.Location = new System.Drawing.Point(483, 310);
            this.txtNumePr.Margin = new System.Windows.Forms.Padding(2);
            this.txtNumePr.Name = "txtNumePr";
            this.txtNumePr.Size = new System.Drawing.Size(121, 20);
            this.txtNumePr.TabIndex = 6;
            // 
            // txtCantitate
            // 
            this.txtCantitate.Location = new System.Drawing.Point(483, 433);
            this.txtCantitate.Margin = new System.Windows.Forms.Padding(2);
            this.txtCantitate.Name = "txtCantitate";
            this.txtCantitate.Size = new System.Drawing.Size(121, 20);
            this.txtCantitate.TabIndex = 7;
            // 
            // txtPret
            // 
            this.txtPret.Location = new System.Drawing.Point(483, 370);
            this.txtPret.Margin = new System.Windows.Forms.Padding(2);
            this.txtPret.Name = "txtPret";
            this.txtPret.Size = new System.Drawing.Size(121, 20);
            this.txtPret.TabIndex = 8;
            // 
            // numepr
            // 
            this.numepr.AutoSize = true;
            this.numepr.Location = new System.Drawing.Point(481, 284);
            this.numepr.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.numepr.Name = "numepr";
            this.numepr.Size = new System.Drawing.Size(45, 13);
            this.numepr.TabIndex = 10;
            this.numepr.Text = "NumePr";
            // 
            // pret
            // 
            this.pret.AutoSize = true;
            this.pret.Location = new System.Drawing.Point(483, 344);
            this.pret.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.pret.Name = "pret";
            this.pret.Size = new System.Drawing.Size(26, 13);
            this.pret.TabIndex = 11;
            this.pret.Text = "Pret";
            // 
            // cantitate
            // 
            this.cantitate.AutoSize = true;
            this.cantitate.Location = new System.Drawing.Point(481, 404);
            this.cantitate.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.cantitate.Name = "cantitate";
            this.cantitate.Size = new System.Drawing.Size(49, 13);
            this.cantitate.TabIndex = 12;
            this.cantitate.Text = "Cantitate";
            // 
            // codD
            // 
            this.codD.AutoSize = true;
            this.codD.Location = new System.Drawing.Point(483, 473);
            this.codD.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.codD.Name = "codD";
            this.codD.Size = new System.Drawing.Size(34, 13);
            this.codD.TabIndex = 13;
            this.codD.Text = "CodD";
            // 
            // buttonFirst
            // 
            this.buttonFirst.Location = new System.Drawing.Point(313, 11);
            this.buttonFirst.Margin = new System.Windows.Forms.Padding(2);
            this.buttonFirst.Name = "buttonFirst";
            this.buttonFirst.Size = new System.Drawing.Size(74, 24);
            this.buttonFirst.TabIndex = 14;
            this.buttonFirst.Text = "First";
            this.buttonFirst.UseVisualStyleBackColor = true;
            this.buttonFirst.Click += new System.EventHandler(this.buttonFirst_Click);
            // 
            // buttonLast
            // 
            this.buttonLast.Location = new System.Drawing.Point(391, 11);
            this.buttonLast.Margin = new System.Windows.Forms.Padding(2);
            this.buttonLast.Name = "buttonLast";
            this.buttonLast.Size = new System.Drawing.Size(74, 24);
            this.buttonLast.TabIndex = 15;
            this.buttonLast.Text = "Last";
            this.buttonLast.UseVisualStyleBackColor = true;
            this.buttonLast.Click += new System.EventHandler(this.buttonLast_Click);
            // 
            // buttonPrevious
            // 
            this.buttonPrevious.Location = new System.Drawing.Point(313, 39);
            this.buttonPrevious.Margin = new System.Windows.Forms.Padding(2);
            this.buttonPrevious.Name = "buttonPrevious";
            this.buttonPrevious.Size = new System.Drawing.Size(74, 24);
            this.buttonPrevious.TabIndex = 16;
            this.buttonPrevious.Text = "Previous";
            this.buttonPrevious.UseVisualStyleBackColor = true;
            this.buttonPrevious.Click += new System.EventHandler(this.buttonPrevious_Click);
            // 
            // buttonNext
            // 
            this.buttonNext.Location = new System.Drawing.Point(391, 39);
            this.buttonNext.Margin = new System.Windows.Forms.Padding(2);
            this.buttonNext.Name = "buttonNext";
            this.buttonNext.Size = new System.Drawing.Size(74, 24);
            this.buttonNext.TabIndex = 17;
            this.buttonNext.Text = "Next";
            this.buttonNext.UseVisualStyleBackColor = true;
            this.buttonNext.Click += new System.EventHandler(this.buttonNext_Click);
            // 
            // labelRecords
            // 
            this.labelRecords.AutoSize = true;
            this.labelRecords.Location = new System.Drawing.Point(503, 33);
            this.labelRecords.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.labelRecords.Name = "labelRecords";
            this.labelRecords.Size = new System.Drawing.Size(47, 13);
            this.labelRecords.TabIndex = 18;
            this.labelRecords.Text = "Records";
            // 
            // txtCodPr
            // 
            this.txtCodPr.Location = new System.Drawing.Point(483, 253);
            this.txtCodPr.Margin = new System.Windows.Forms.Padding(2);
            this.txtCodPr.Name = "txtCodPr";
            this.txtCodPr.Size = new System.Drawing.Size(121, 20);
            this.txtCodPr.TabIndex = 19;
            // 
            // codpr
            // 
            this.codpr.AutoSize = true;
            this.codpr.Location = new System.Drawing.Point(481, 229);
            this.codpr.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.codpr.Name = "codpr";
            this.codpr.Size = new System.Drawing.Size(36, 13);
            this.codpr.TabIndex = 20;
            this.codpr.Text = "CodPr";
            // 
            // comboBoxCodD
            // 
            this.comboBoxCodD.FormattingEnabled = true;
            this.comboBoxCodD.Location = new System.Drawing.Point(483, 494);
            this.comboBoxCodD.Name = "comboBoxCodD";
            this.comboBoxCodD.Size = new System.Drawing.Size(121, 21);
            this.comboBoxCodD.TabIndex = 21;
            // 
            // buttonExit
            // 
            this.buttonExit.Location = new System.Drawing.Point(103, 27);
            this.buttonExit.Name = "buttonExit";
            this.buttonExit.Size = new System.Drawing.Size(75, 23);
            this.buttonExit.TabIndex = 22;
            this.buttonExit.Text = "Exit";
            this.buttonExit.UseVisualStyleBackColor = true;
            this.buttonExit.Click += new System.EventHandler(this.buttonExit_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(620, 527);
            this.Controls.Add(this.buttonExit);
            this.Controls.Add(this.comboBoxCodD);
            this.Controls.Add(this.codpr);
            this.Controls.Add(this.txtCodPr);
            this.Controls.Add(this.labelRecords);
            this.Controls.Add(this.buttonNext);
            this.Controls.Add(this.buttonPrevious);
            this.Controls.Add(this.buttonLast);
            this.Controls.Add(this.buttonFirst);
            this.Controls.Add(this.codD);
            this.Controls.Add(this.cantitate);
            this.Controls.Add(this.pret);
            this.Controls.Add(this.numepr);
            this.Controls.Add(this.txtPret);
            this.Controls.Add(this.txtCantitate);
            this.Controls.Add(this.txtNumePr);
            this.Controls.Add(this.buttonDelete);
            this.Controls.Add(this.buttonUpdate);
            this.Controls.Add(this.buttonAdd);
            this.Controls.Add(this.dataGridViewChild);
            this.Controls.Add(this.dataGridViewParent);
            this.Controls.Add(this.connect);
            this.Margin = new System.Windows.Forms.Padding(2);
            this.Name = "Form1";
            this.Text = "Form1";
            ((System.ComponentModel.ISupportInitialize)(this.dataGridViewParent)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridViewChild)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button connect;
        private System.Windows.Forms.DataGridView dataGridViewParent;
        private System.Windows.Forms.DataGridView dataGridViewChild;
        private System.Windows.Forms.Button buttonAdd;
        private System.Windows.Forms.Button buttonUpdate;
        private System.Windows.Forms.Button buttonDelete;
        private System.Windows.Forms.TextBox txtNumePr;
        private System.Windows.Forms.TextBox txtCantitate;
        private System.Windows.Forms.TextBox txtPret;
        private System.Windows.Forms.Label numepr;
        private System.Windows.Forms.Label pret;
        private System.Windows.Forms.Label cantitate;
        private System.Windows.Forms.Label codD;
        private System.Windows.Forms.Button buttonFirst;
        private System.Windows.Forms.Button buttonLast;
        private System.Windows.Forms.Button buttonPrevious;
        private System.Windows.Forms.Button buttonNext;
        private System.Windows.Forms.Label labelRecords;
        private System.Windows.Forms.TextBox txtCodPr;
        private System.Windows.Forms.Label codpr;
        private System.Windows.Forms.ComboBox comboBoxCodD;
        private System.Windows.Forms.Button buttonExit;
    }
}

