create database if not exists Mania_hotel;
USE Mania_hotel;

DROP TABLE IF EXISTS 'utilisateurs';
CREATE TABLE utilisateurs(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(200) NOT NULL,
    email VARCHAR(200) UNIQUE NOT NULL,
    mot_de_passe VARCHAR(200) NOT NULL,
    role ENUM ("gerant","receptioniste")
);

DROP TABLE IF EXISTS 'clients';
CREATE TABLE clients(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(200) NOT NULL,
    email VARCHAR(200) UNIQUE NOT NULL,
    telephone INT
);

DROP TABLE IF EXISTS 'chambres';
CREATE TABLE chambres(
    id INT AUTO_INCREMENT PRIMARY KEY,
    type VARCHAR(200),
    numero_chambre INT
);

DROP TABLE IF EXISTS 'reservations';
CREATE TABLE reservations(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(200) NOT NULL,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    id_chambre INT,
    id_client INT,
    reserver VARCHAR(200),
    FOREIGN KEY id_chambre REFERENCES chambres(id) ON DELETE CASCADE,
    FOREIGN KEY id_client REFERENCES clients(id) ON DELETE CASCADE
);