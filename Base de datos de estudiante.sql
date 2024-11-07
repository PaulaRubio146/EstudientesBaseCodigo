
CREATE DATABASE escuela;

USE escuela;
CREATE TABLE DistanciasEstudiantes (
    cedula VARCHAR(20) PRIMARY KEY,
    nombres VARCHAR(50),
    apellidos VARCHAR(50),
    distancia FLOAT
);


CREATE TABLE Estudiantes (
    cedulas VARCHAR(20) PRIMARY KEY,
    nombres VARCHAR(50),
    apellidos VARCHAR(50),
    direccionResidencia TEXT,
    coordenadasResidencia POINT,  -- datos espaciales
    direccionTrabajo TEXT,
    coordenadasTrabajo POINT      -- datos espaciales
);


DELIMITER //
CREATE TRIGGER calcular_distancia
AFTER INSERT ON Estudiantes
FOR EACH ROW
BEGIN
    DECLARE distancia_calculada FLOAT;

    -- Calcula la distancia usando las coordenadas insertadas
    SET distancia_calculada = ST_Distance_Sphere(NEW.coordenadasResidencia, NEW.coordenadasTrabajo);

    -- Inserta los datos en la tabla DistanciasEstudiantes
    INSERT INTO DistanciasEstudiantes (cedula, nombres, apellidos, distancia)
    VALUES (NEW.cedulas, NEW.nombres, NEW.apellidos, distancia_calculada);
END;
//

DELIMITER ;
   

DELIMITER //

CREATE PROCEDURE InsertarEstudiante(
    IN p_cedulas VARCHAR(20),
    IN p_nombres VARCHAR(50),
    IN p_apellidos VARCHAR(50),
    IN p_direccionResidencia TEXT,
    IN p_latResidencia DOUBLE,
    IN p_lonResidencia DOUBLE,
    IN p_direccionTrabajo TEXT,
    IN p_latTrabajo DOUBLE,
    IN p_lonTrabajo DOUBLE
)
BEGIN
    -- Inserta el nuevo registro en la tabla Estudiantes
    INSERT INTO Estudiantes (cedulas, nombres, apellidos, direccionResidencia, coordenadasResidencia, direccionTrabajo, coordenadasTrabajo)
    VALUES (
        p_cedulas, 
        p_nombres, 
        p_apellidos, 
        p_direccionResidencia, 
        POINT(p_latResidencia, p_lonResidencia), 
        p_direccionTrabajo, 
        POINT(p_latTrabajo, p_lonTrabajo)
    );
END;
//

DELIMITER ;

DELIMITER //

CREATE PROCEDURE ObtenerEstudiantesConDistancia()
BEGIN
    SELECT 
        cedulas, 
        nombres, 
        apellidos, 
        direccionResidencia, 
        direccionTrabajo, 
        ST_Distance_Sphere(coordenadasResidencia, coordenadasTrabajo) AS distance
    FROM 
        Estudiantes
    ORDER BY 
        distance ASC;
END;
//

DELIMITER ;

