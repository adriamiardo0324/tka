CREATE TABLE utilisateurs(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(200) NOT NULL,
    email VARCHAR(200) UNIQUE NOT NULL,
    mot_de_passe VARCHAR(200) NOT NULL,
    role ENUM ("gerant","receptioniste")
);

CREATE TABLE clients(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(200) NOT NULL,
    email VARCHAR(200) UNIQUE NOT NULL,
    telephone INT
);

CREATE TABLE chambres(
    id INT AUTO_INCREMENT PRIMARY KEY,
    type VARCHAR(200),
);

CREATE TABLE reservation(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(200) NOT NULL,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    id_chambre INT,
    reserver VARCHAR(200),
    FOREIGN KEY id_chambre REFERENCES chambres(id) ON DELETE CASCADE
);