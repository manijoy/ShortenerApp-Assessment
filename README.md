# ShorterApp

This project was generated with [Angular CLI](https://github.com/angular/angular-cli) version 13.0.2.

## Development server

Run `ng serve` for a dev server. Navigate to `http://localhost:4200/`. The app will automatically reload if you change any of the source files.

## MYSQL Database & Table Creation
Create database urldb

CREATE TABLE `urls` (
  `id` int NOT NULL AUTO_INCREMENT,
  `shorturl` varchar(45) NOT NULL,
  `longurl` varchar(255) NOT NULL,
  `hitcount` int(10) unsigned zerofill NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `shorturl_UNIQUE` (`shorturl`),
  UNIQUE KEY `longurl_UNIQUE` (`longurl`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

## Python Flask Server Up & Runnin

1)Install all dependent modules using requirements.txt(find file in /api folder): 
  ## pip install -r requirements.txt
2) Start the Flask application using below command:
  ## python urls.py
