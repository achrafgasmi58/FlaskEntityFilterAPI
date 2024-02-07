from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Liste(db.Model):
    __tablename__ = 'liste'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Prenom = db.Column(db.Text, nullable=True)
    Nom = db.Column(db.Text, nullable=True)
    Date_de_naissance = db.Column(db.Date, nullable=True)
    Lieu_de_naissance = db.Column(db.Text, nullable=True)
    Nationalite = db.Column(db.Text, nullable=True)
    Cin = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"<Liste(id={self.id}, Prenom='{self.Prenom}', Nom='{self.Nom}', Date_de_naissance='{self.Date_de_naissance}', Lieu_de_naissance='{self.Lieu_de_naissance}', Nationalite='{self.Nationalite}', Cin='{self.Cin}')>"

class ListeMorale(db.Model):
    __tablename__ = 'listeMorale'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Prenom = db.Column(db.Text, nullable=True)
    Nom = db.Column(db.Text, nullable=True)
    Date_de_naissance = db.Column(db.Date, nullable=True)
    Lieu_de_naissance = db.Column(db.Text, nullable=True)
    Nationalite = db.Column(db.Text, nullable=True)
    Cin = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"<ListeMorale(id={self.id}, Prenom='{self.Prenom}', Nom='{self.Nom}', Date_de_naissance='{self.Date_de_naissance}', Lieu_de_naissance='{self.Lieu_de_naissance}', Nationalite='{self.Nationalite}', Cin='{self.Cin}')>"

class PepThomsonIndiv(db.Model):
    __tablename__ = 'PepThomsonIndiv'
    UID = db.Column(db.Integer, primary_key=True)
    Category = db.Column(db.String(50), nullable=True)
    EnteredDate = db.Column(db.Date, nullable=True)
    UpdatedDate = db.Column(db.Date, nullable=True)
    Title = db.Column(db.String(100), nullable=True)
    Position = db.Column(db.String(255), nullable=True)
    FirstName = db.Column(db.String(100), nullable=True)
    LastName = db.Column(db.String(100), nullable=True)
    DOB = db.Column(db.Date, nullable=True)

    def __repr__(self):
        return f"<PepThomsonIndiv(UID={self.UID}, Category='{self.Category}', EnteredDate='{self.EnteredDate}', UpdatedDate='{self.UpdatedDate}', Title='{self.Title}', Position='{self.Position}', FirstName='{self.FirstName}', LastName='{self.LastName}', DOB='{self.DOB}')>"
