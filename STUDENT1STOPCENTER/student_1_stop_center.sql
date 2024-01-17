-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 17, 2024 at 03:43 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `student_1_stop_center`
--

-- --------------------------------------------------------

--
-- Table structure for table `course`
--

CREATE TABLE `course` (
  `Level_of_Study` varchar(10) NOT NULL,
  `Program` varchar(10) NOT NULL,
  `Semester` int(1) NOT NULL,
  `Subject_Code` varchar(6) NOT NULL,
  `Subject_Name` varchar(255) NOT NULL,
  `Lecturer_Name` varchar(255) NOT NULL,
  `Credit_Hour` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `grade_semester1`
--

CREATE TABLE `grade_semester1` (
  `student_id` int(10) NOT NULL,
  `course_code` varchar(6) NOT NULL,
  `credit_hours` varchar(3) NOT NULL,
  `grade` varchar(1) NOT NULL,
  `gpa` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `grade_semester2`
--

CREATE TABLE `grade_semester2` (
  `student_id` int(10) NOT NULL,
  `course_code` varchar(6) NOT NULL,
  `credit_hours` varchar(3) NOT NULL,
  `grade` varchar(1) NOT NULL,
  `gpa` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `grade_semester3`
--

CREATE TABLE `grade_semester3` (
  `student_id` int(10) NOT NULL,
  `course_code` varchar(6) NOT NULL,
  `credit_hours` varchar(3) NOT NULL,
  `grade` varchar(1) NOT NULL,
  `gpa` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `grade_semester4`
--

CREATE TABLE `grade_semester4` (
  `student_id` int(10) NOT NULL,
  `course_code` varchar(6) NOT NULL,
  `credit_hours` varchar(3) NOT NULL,
  `grade` varchar(1) NOT NULL,
  `gpa` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `grade_semester5`
--

CREATE TABLE `grade_semester5` (
  `student_id` int(10) NOT NULL,
  `course_code` varchar(6) NOT NULL,
  `credit_hours` varchar(3) NOT NULL,
  `grade` varchar(1) NOT NULL,
  `gpa` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `Stu_ID` varchar(10) NOT NULL,
  `Stu_DOB` date NOT NULL,
  `Stu_Title` varchar(10) NOT NULL,
  `Stu_FName` varchar(30) NOT NULL,
  `Stu_LName` varchar(30) NOT NULL,
  `Stu_Age` int(3) NOT NULL,
  `Stu_Gender` varchar(6) NOT NULL,
  `Stu_Level_of_Study` varchar(8) NOT NULL,
  `Stu_Sem` int(1) NOT NULL,
  `Stu_Group` varchar(10) NOT NULL,
  `Stu_Program` varchar(7) NOT NULL,
  `Stu_Faculty` varchar(50) NOT NULL,
  `Stu_Institution` varchar(20) NOT NULL,
  `Stu_Address` varchar(50) NOT NULL,
  `Stu_Phone` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
