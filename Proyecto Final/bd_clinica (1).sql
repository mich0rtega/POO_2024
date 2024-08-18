-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 18-08-2024 a las 22:44:57
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bd_clinica`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `diagnosticos`
--

CREATE TABLE `diagnosticos` (
  `id` int(11) NOT NULL,
  `id_paciente` int(11) NOT NULL,
  `diagnostico` text NOT NULL,
  `receta` text NOT NULL,
  `fecha_registro` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `diagnosticos`
--

INSERT INTO `diagnosticos` (`id`, `id_paciente`, `diagnostico`, `receta`, `fecha_registro`) VALUES
(1, 1, 'tos', 'ketorolaco', '2024-08-18 11:55:27');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `enfermeros`
--

CREATE TABLE `enfermeros` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `apellidos` varchar(255) NOT NULL,
  `numEmpleado` varchar(7) NOT NULL,
  `password` varchar(255) NOT NULL,
  `area` varchar(255) NOT NULL,
  `turno` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `enfermeros`
--

INSERT INTO `enfermeros` (`id`, `nombre`, `apellidos`, `numEmpleado`, `password`, `area`, `turno`) VALUES
(1, 'Edwin', 'Ortega', '13', '3dfbf1fbdbf9d2eb39e14955dcfd073792ebed8c9b97995210e70c4059be13c9', 'pediatria', 'matutino');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `medicos`
--

CREATE TABLE `medicos` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `apellidos` varchar(255) NOT NULL,
  `numEmpleado` varchar(7) NOT NULL,
  `password` varchar(255) NOT NULL,
  `especialidad` varchar(255) NOT NULL,
  `turno` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `medicos`
--

INSERT INTO `medicos` (`id`, `nombre`, `apellidos`, `numEmpleado`, `password`, `especialidad`, `turno`) VALUES
(1, 'Juan', 'Perez', '12', 'ed08c290d7e22f7bb324b15cbadce35b0b348564fd2d5f95752388d86d71bcca', 'cardiologia', 'matutino');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pacientes`
--

CREATE TABLE `pacientes` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `edad` int(11) NOT NULL,
  `sexo` varchar(50) NOT NULL,
  `tipo_sangre` varchar(50) NOT NULL,
  `altura` float NOT NULL,
  `peso` float NOT NULL,
  `alergias` text DEFAULT NULL,
  `numero_cama` int(11) NOT NULL,
  `id_medico` int(11) NOT NULL,
  `id_enfermero` int(11) NOT NULL,
  `fecha_registro` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `pacientes`
--

INSERT INTO `pacientes` (`id`, `nombre`, `edad`, `sexo`, `tipo_sangre`, `altura`, `peso`, `alergias`, `numero_cama`, `id_medico`, `id_enfermero`, `fecha_registro`) VALUES
(1, 'Liam', 55, 'masc', 'ab+', 1.78, 68, 'n/h', 76, 1, 1, '2024-08-18 11:54:56'),
(3, 'miryam', 44, 'fem', 'b+', 1.56, 55, 'polen', 67, 1, 1, '2024-08-18 11:57:22');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `signos_vitales`
--

CREATE TABLE `signos_vitales` (
  `id` int(11) NOT NULL,
  `id_paciente` int(11) NOT NULL,
  `temperatura` float NOT NULL,
  `presion_sistolica` int(11) NOT NULL,
  `presion_diastolica` int(11) NOT NULL,
  `pulso` int(11) NOT NULL,
  `estado` varchar(10) DEFAULT NULL,
  `fecha_registro` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `signos_vitales`
--

INSERT INTO `signos_vitales` (`id`, `id_paciente`, `temperatura`, `presion_sistolica`, `presion_diastolica`, `pulso`, `estado`, `fecha_registro`) VALUES
(1, 3, 36.1, 120, 80, 88, 'Normal', '2024-08-18 11:59:09');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `diagnosticos`
--
ALTER TABLE `diagnosticos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_paciente` (`id_paciente`);

--
-- Indices de la tabla `enfermeros`
--
ALTER TABLE `enfermeros`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`numEmpleado`);

--
-- Indices de la tabla `medicos`
--
ALTER TABLE `medicos`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`numEmpleado`);

--
-- Indices de la tabla `pacientes`
--
ALTER TABLE `pacientes`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_medico` (`id_medico`,`id_enfermero`),
  ADD KEY `id_enfermero` (`id_enfermero`);

--
-- Indices de la tabla `signos_vitales`
--
ALTER TABLE `signos_vitales`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_paciente` (`id_paciente`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `diagnosticos`
--
ALTER TABLE `diagnosticos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `enfermeros`
--
ALTER TABLE `enfermeros`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `medicos`
--
ALTER TABLE `medicos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `pacientes`
--
ALTER TABLE `pacientes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `signos_vitales`
--
ALTER TABLE `signos_vitales`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `diagnosticos`
--
ALTER TABLE `diagnosticos`
  ADD CONSTRAINT `diagnosticos_ibfk_1` FOREIGN KEY (`id_paciente`) REFERENCES `pacientes` (`id`);

--
-- Filtros para la tabla `pacientes`
--
ALTER TABLE `pacientes`
  ADD CONSTRAINT `pacientes_ibfk_1` FOREIGN KEY (`id_medico`) REFERENCES `medicos` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `pacientes_ibfk_2` FOREIGN KEY (`id_enfermero`) REFERENCES `enfermeros` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `signos_vitales`
--
ALTER TABLE `signos_vitales`
  ADD CONSTRAINT `signos_vitales_ibfk_1` FOREIGN KEY (`id_paciente`) REFERENCES `pacientes` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
