-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 27, 2023 at 04:48 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `recommendationsport`
--

-- --------------------------------------------------------

--
-- Table structure for table `bookingcourt`
--

CREATE TABLE `bookingcourt` (
  `order_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `sportsCentre` varchar(255) NOT NULL,
  `location` varchar(255) NOT NULL,
  `sportsCourt` varchar(255) NOT NULL,
  `courtName` varchar(255) NOT NULL,
  `dateBooking` date NOT NULL,
  `time` time NOT NULL DEFAULT current_timestamp(),
  `timeFinish` time NOT NULL,
  `duration` int(11) NOT NULL,
  `totalPrice` float(10,2) NOT NULL,
  `rating` int(11) NOT NULL,
  `custName` varchar(255) NOT NULL,
  `phoneNumber` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `bookingcourt`
--

INSERT INTO `bookingcourt` (`order_id`, `user_id`, `sportsCentre`, `location`, `sportsCourt`, `courtName`, `dateBooking`, `time`, `timeFinish`, `duration`, `totalPrice`, `rating`, `custName`, `phoneNumber`) VALUES
(1, 1, 'Jebat Racquet Sports Centre', 'Melaka', 'Badminton', '1', '2022-12-17', '14:00:00', '00:00:00', 1, 150.00, 3, 'Fitri', '0176193230'),
(3, 1, 'Sports Complex Batu Berendam', 'Melaka', 'Badminton', '1', '2022-12-21', '15:00:00', '00:00:00', 2, 100.00, 4, 'Fitri', '0176193230'),
(5, 4, 'Sports Complex Batu Berendam', 'Melaka', 'Futsal', '3', '2022-12-21', '14:00:00', '17:00:00', 3, 100.00, 0, 'Fauzan', '0127749219'),
(6, 5, 'Futsal Future Sport Centre', 'Pulau Pinang', 'Futsal', '5', '2022-12-21', '16:00:00', '17:00:00', 1, 40.00, 0, 'Irfan', '0193329906'),
(7, 2, 'Jempol Futsal Galaxy', 'Negeri Sembilan', 'Futsal', '4', '2022-12-21', '13:00:00', '17:00:00', 4, 50.00, 0, 'Faris', '0194432573'),
(30, 1, 'Sports Complex Batu Berendam', 'Melaka', 'Badminton', '3', '2023-01-21', '15:00:00', '17:00:00', 2, 50.00, 4, 'Fitri', '0176193230'),
(33, 1, 'Lavana Sports Centre', 'Kuala Lumpur', 'Badminton', '3', '2023-01-24', '18:00:00', '21:00:00', 3, 50.00, 3, 'Fitri', '0176193230'),
(37, 2, 'Kompleks Sukan MPSP Bertam', 'Pulau Pinang', 'Badminton', '3', '2023-02-01', '00:00:00', '02:00:00', 2, 30.00, 0, 'Faris', '0194432573'),
(42, 1, 'Dewan Badminton MSN', 'Melaka', 'Badminton', '2', '2023-01-26', '16:00:00', '18:00:00', 2, 60.00, 3, 'Fitri', '0176193230'),
(44, 1, 'Sports Complex Batu Berendam', 'Melaka', 'Badminton', '3', '2023-02-02', '13:00:00', '15:00:00', 2, 45.00, 4, 'Fitri', '0176193230'),
(46, 1, 'Batu Berendam Badminton Hall', 'Melaka', 'Badminton', '3', '2023-02-09', '19:00:00', '21:00:00', 2, 30.00, 3, 'Fitri', '0176193230'),
(48, 1, 'Kompleks Sukan Bangsar', 'Kuala Lumpur', 'Badminton', '2', '2023-02-14', '16:00:00', '18:00:00', 2, 60.00, 4, 'Fitri', '0176193230'),
(51, 11, 'Kompleks Sukan Setiawangsa', 'Kuala Lumpur', 'Badminton', '3', '2023-02-16', '18:00:00', '20:00:00', 2, 30.00, 3, 'Kasim', '0195559830'),
(52, 1, 'Frenzy Sports Arena', 'Selangor', 'Futsal', '3', '2023-02-19', '19:00:00', '21:00:00', 2, 60.00, 5, 'Fitri', '0176193230'),
(53, 1, '222 Sports Centre PJ', 'Selangor', 'Badminton', '2', '2023-02-23', '15:00:00', '17:00:00', 2, 60.00, 3, 'Fitri', '0176193230'),
(57, 12, 'Permata Sports Complex', 'Pulau Pinang', 'Tennis', '2', '2023-02-25', '19:00:00', '22:00:00', 3, 130.00, 4, 'Afifi', '0195543278'),
(58, 12, 'Jebat Racquet Sports Centre', 'Melaka', 'Badminton', '3', '2023-02-27', '18:00:00', '21:00:00', 3, 105.00, 3, 'Afifi', '0195543278'),
(59, 12, 'Sports Complex Batu Berendam', 'Melaka', 'Futsal', '2', '2023-02-28', '22:00:00', '00:00:00', 2, 175.00, 4, 'Afifi', '0195543278'),
(60, 12, 'Kompleks Maksak', 'Melaka', 'Squash', '3', '2023-03-02', '22:00:00', '00:00:00', 2, 90.00, 4, 'Afifi', '0195543278'),
(61, 12, 'KRM Maran', 'Pahang', 'Volleyball', '2', '2023-03-04', '15:00:00', '19:00:00', 4, 130.00, 4, 'Afifi', '0195543278'),
(64, 15, 'Batu Berendam Badminton Hall', 'Melaka', 'Badminton', '3', '2023-02-22', '21:00:00', '23:00:00', 2, 40.00, 0, 'AFIQ JALIL', '0178769325'),
(65, 16, 'KOMBES KL', 'Kuala Lumpur', 'Futsal', '2', '2023-02-22', '19:00:00', '21:00:00', 2, 190.00, 0, 'sharifah', '0146679806');

-- --------------------------------------------------------

--
-- Table structure for table `staff`
--

CREATE TABLE `staff` (
  `staff_id` int(11) NOT NULL,
  `sportsCentre` varchar(255) NOT NULL,
  `location` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `staff`
--

INSERT INTO `staff` (`staff_id`, `sportsCentre`, `location`, `password`) VALUES
(1, 'Dewan Badminton Berapit', 'Pulau Pinang', '1000'),
(2, 'Kompleks Belia dan Sukan Penang', 'Pulau Pinang', '2000'),
(3, 'Gembira Parade Futsal Court', 'Pulau Pinang', '3000'),
(4, 'Permata Sports Complex', 'Pulau Pinang', '4000'),
(5, 'BB Futsal', 'Pulau Pinang', '5000'),
(6, 'Best Bola Bola Sports Centre', 'Pulau Pinang', '6000'),
(7, 'Dewan Badminton Bukit Dumbar PBA', 'Pulau Pinang', '7000'),
(8, 'Kompleks Sukan MPSP Bertam', 'Pulau Pinang', '8000'),
(9, 'Nicol David International Squash Centre', 'Pulau Pinang', '9000'),
(10, 'NSC Futsal', 'Pulau Pinang', '1001'),
(11, 'Kompleks Sukan Titi Mukim', 'Pulau Pinang', '1100'),
(12, 'Fiz Futsal Penang', 'Pulau Pinang', '1200'),
(13, 'Kompleks Sukan dan Komuniti Pinang Tunggal', 'Pulau Pinang', '1300'),
(14, 'LTT Badminton Court & Training Centre', 'Pulau Pinang', '1400'),
(15, 'JesselBall Sport Centre', 'Pulau Pinang', '1500'),
(16, 'Futsal Future Sport Centre', 'Pulau Pinang', '1600'),
(17, 'MBPP Relau Sport Complex', 'Pulau Pinang', '1700'),
(18, 'Sunway Sports Center', 'Pulau Pinang', '1800'),
(19, 'Kompleks Sukan Bandaraya Relau', 'Pulau Pinang', '1900'),
(20, 'C & Y Sport Centre', 'Pulau Pinang', '2001'),
(21, 'Titi Mukim Sports Complex', 'Pulau Pinang', '2100'),
(22, 'Kompleks Sukan & Rekreasi Sony Seberang Jaya', 'Pulau Pinang', '2200'),
(23, 'New Town Sport Center', 'Pulau Pinang', '2300'),
(24, 'Osp Badminton Hall', 'Pulau Pinang', '2400'),
(25, 'Futsal Kick Off', 'Pulau Pinang', '2500'),
(26, 'Kompleks Sukan dan Komuniti Jerlun', 'Kedah', '2600'),
(27, 'Kompleks Sukan dan Bandar Baru', 'Kedah', '2700'),
(28, 'Kompleks Rakan Muda, Baling', 'Kedah', '2800'),
(29, 'Amanjaya Sport Centre', 'Kedah', '2900'),
(30, 'Gelanggang Badminton Kulim CRC', 'Kedah', '3001'),
(31, 'Sena Sports Central', 'Kedah', '3100'),
(32, 'Gmee Futsal Sport Centre', 'Kedah', '3200'),
(33, 'Pusat Rakan Sukan Pendang', 'Kedah', '3300'),
(34, 'Kompleks Sukan Langkawi', 'Kedah', '3400'),
(35, 'Elite PRO Sports Centre', 'Kedah', '3500'),
(36, 'Q-In Sports Centre', 'Kedah', '3600'),
(37, 'Darulaman Sport Arena', 'Kedah', '3700'),
(38, 'KHTP Sports Complex', 'Kedah', '3800'),
(39, 'CT Sports Arena', 'Kedah', '3900'),
(40, 'Kompleks Sukan Kulim Hitech', 'Kedah', '4001'),
(41, 'CT Advance Sports', 'Kedah', '4100'),
(42, 'WIRASPORTS', 'Kedah', '4200'),
(43, 'SMC Futsal', 'Kedah', '4300'),
(44, 'ASRC Badminton Court', 'Kedah', '4400'),
(45, 'WNS Futsal Centre', 'Kedah', '4500'),
(46, 'Northern Futsal Center', 'Kedah', '4600'),
(47, 'MHZ Badminton Centre', 'Kedah', '4700'),
(48, 'SNA Sport Centre', 'Kedah', '4800'),
(49, 'MRC Badminton Hall, Desa Kiara', 'Kedah', '4900'),
(50, 'Kombes Perlis', 'Perlis', '5001'),
(51, 'R7 Futsal Centre', 'Perlis', '5100'),
(52, 'D\' Futsal Center', 'Perlis', '5200'),
(53, 'MO Q Sport Arena', 'Perlis', '5300'),
(54, 'All In Sport Centre', 'Perlis', '5400'),
(55, 'Kompleks Sukan dan Komuniti Sungai Siput', 'Perak', '5500'),
(56, 'Asia Futsal Center', 'Perak', '5600'),
(57, 'Kompleks Sukan Tapah', 'Perak', '5700'),
(58, 'Arena Square Kampung Tanjung Keramat', 'Perak', '5800'),
(59, 'Gelanggang Futsal Bukit Gantang', 'Perak', '5900'),
(60, 'Sportizza Futsal Arena Menglembu', 'Perak', '6001'),
(61, 'Manjung Indoor Sports Arena', 'Perak', '6100'),
(62, 'Dss Futsal Centre', 'Perak', '6200'),
(63, 'Dynamic Futsal', 'Perak', '6301'),
(64, 'Falim Sports Centre', 'Perak', '6400'),
(65, 'MP3 Sports Centre', 'Perak', '6500'),
(66, 'Sport Complex Grand Kampar', 'Perak', '6600'),
(67, 'Anson Sport Centre', 'Perak', '6700'),
(68, 'Kampar Badminton Sentral', 'Perak', '6800'),
(69, 'X Park Sunway City Ipoh', 'Perak', '6900'),
(70, 'Yc Badminton Centre', 'Perak', '7001'),
(71, '3D Futsal Centre', 'Perak', '7100'),
(72, 'Younique Sports Ampang Ipoh', 'Perak', '7200'),
(73, 'Arena Badminton Perak', 'Perak', '7300'),
(74, 'Winning Futsal', 'Perak', '7400'),
(75, 'Silver Fox Futsal', 'Perak', '7500'),
(76, 'T. Z.Y Sport Arena', 'Perak', '7600'),
(77, 'Kok Bou Badminton Court', 'Perak', '7700'),
(78, 'Dewan Badminton Bandar Lahat Baru', 'Perak', '7800'),
(79, 'D\' Legend Badminton Court', 'Perak', '7900'),
(80, 'Pro Sport Futsal Arena', 'Perak', '8001'),
(81, 'Kompleks Sukan dan Komuniti Simpang Pertang', 'Negeri Sembilan', '8100'),
(82, 'KOMBES Paroi', 'Negeri Sembilan', '8200'),
(83, 'Center Court Kompleks Sukan Negeri', 'Negeri Sembilan', '8300'),
(84, 'Micheal\'s Badminton Academy', 'Negeri Sembilan', '8400'),
(85, 'KRM Kuala Pilah', 'Negeri Sembilan', '8500'),
(86, 'KRM Jempol', 'Negeri Sembilan', '8600'),
(87, 'GR Sports Centre', 'Negeri Sembilan', '8700'),
(88, 'Summer Sport Centre', 'Negeri Sembilan', '8800'),
(89, 'Sendayan Sport Centre', 'Negeri Sembilan', '8900'),
(90, 'DreamBadminton Sports Complex Nilai', 'Negeri Sembilan', '9001'),
(91, 'Dewan Bahau Storm Badminton Sport Centre', 'Negeri Sembilan', '9100'),
(92, 'All Stars Futsal', 'Negeri Sembilan', '9200'),
(93, 'Public Star Futsal', 'Negeri Sembilan', '9300'),
(94, 'X Park Sendayan', 'Negeri Sembilan', '9400'),
(95, 'Ultimate Sporthaus', 'Negeri Sembilan', '9500'),
(96, 'Jempol Futsal Galaxy', 'Negeri Sembilan', '9600'),
(97, 'Kompleks Sukan dan Komuniti Krubong', 'Melaka', '9700'),
(98, 'Dewan Badminton MSN', 'Melaka', '9800'),
(99, 'Gelanggang AKA Futsal Centre', 'Melaka', '9900'),
(100, 'Dewan Badminton Seri Pandan', 'Melaka', '1011'),
(101, 'Sports Complex Batu Berendam', 'Melaka', '1010'),
(102, 'Malim Sports Centre', 'Melaka', '1020'),
(103, 'Jebat Racquet Sports Centre', 'Melaka', '1030'),
(104, 'Yu Hwa Badminton Hall', 'Melaka', '1040'),
(105, 'Futsal A Sports Arena', 'Melaka', '1050'),
(106, 'Centre Point Badminton Court', 'Melaka', '1060'),
(107, 'Kompleks Maksak', 'Melaka', '1070'),
(108, 'Batu Berendam Badminton Hall', 'Melaka', '1080'),
(109, 'Sport Planet Futsal Cheng', 'Melaka', '1090'),
(110, 'JO Badminton Hall', 'Melaka', '1100'),
(111, 'Heng Ann Badminton Hall', 'Melaka', '1110'),
(112, 'Dewan Badminton MAKSAK', 'Melaka', '1120'),
(113, 'Kompleks Sukan dan Komuniti Kundang Ulu', 'Johor', '1130'),
(114, 'Kompleks Sukan dan Komuniti Bandar Penawar', 'Johor', '1140'),
(115, 'Kompleks MSN Pagoh', 'Johor', '1150'),
(116, 'Stadium Futsal Pontian', 'Johor', '1160'),
(117, 'Y Centre UTC JOHOR', 'Johor', '1170'),
(118, 'PB Futsal', 'Johor', '1180'),
(119, 'Gelanggang Futsal Majlis Daerah Tangkak', 'Johor', '1190'),
(120, 'Daiman Sports Complex', 'Johor', '1200'),
(121, 'Millennium Sports Center', 'Johor', '1210'),
(122, 'Daiman Sri Skudai Sports Center', 'Johor', '1220'),
(123, 'Tebrau Sport & Recreation Centre', 'Johor', '1230'),
(124, 'Sutera Sports World', 'Johor', '1240'),
(125, 'Just In Sports Centre', 'Johor', '1250'),
(126, 'Permas Jaya Sports Complex', 'Johor', '1260'),
(127, 'Pekan Nanas Sports Centre', 'Johor', '1270'),
(128, 'U Five Sports', 'Johor', '1280'),
(129, 'TS Sport Complex Sdn. Bhd.', 'Johor', '1290'),
(130, 'Hot Sports Arena', 'Johor', '1300'),
(131, 'Golden Sports Center', 'Johor', '1310'),
(132, 'Bubble Sports Complex Tebrau', 'Johor', '1320'),
(133, 'Sri Amar JL Sports Centre', 'Johor', '1330'),
(134, 'Too Bee Sport Centre', 'Johor', '1340'),
(135, 'Tiara Sports World', 'Johor', '1350'),
(136, 'Impian Sports', 'Johor', '1360'),
(137, 'Sports Prima Sdn Bhd', 'Johor', '1370'),
(138, 'C & Y Badminton Court', 'Johor', '1380'),
(139, 'Desa Mutiara Sports Arena', 'Johor', '1390'),
(140, 'Victory Sports Centre', 'Johor', '1400'),
(141, 'Dewan Badminton DJ Sport', 'Johor', '1410'),
(142, 'KC Futsal', 'Johor', '1420'),
(143, 'Everyday Sports', 'Johor', '1430'),
(144, 'Kompleks Sukan dan Komuniti Pekan', 'Pahang', '1440'),
(145, 'Kompleks Sukan dan Komuniti Mempaga', 'Pahang', '1450'),
(146, 'Kompleks MSN Kuala Rompin', 'Pahang', '1460'),
(147, 'One Touch Futsal', 'Pahang', '1470'),
(148, 'KRM Raub', 'Pahang', '1480'),
(149, 'KRM Maran', 'Pahang', '1490'),
(150, 'PlayGround No. 6 Sport Centre', 'Pahang', '1500'),
(151, 'Kompleks Sukpa', 'Pahang', '1510'),
(152, 'Kompleks Rakan Muda Sukan Air Rompin', 'Pahang', '1520'),
(153, 'Jengka Sports Centre', 'Pahang', '1530'),
(154, 'Semambu Badminton Centre', 'Pahang', '1540'),
(155, 'Kuantan Synergy Sports Centre', 'Pahang', '1550'),
(156, 'Kilang Futsal Sungai Isap', 'Pahang', '1560'),
(157, 'AD Sport Futsal Centre', 'Pahang', '1570'),
(158, 'Mempaga Community Sports Complex', 'Pahang', '1580'),
(159, 'NS7 Sport Centre', 'Pahang', '1590'),
(160, 'MK Badminton Centre', 'Pahang', '1600'),
(161, 'Chendering Futsal', 'Pahang', '1610'),
(162, 'Jerantut Badminton Centre', 'Pahang', '1620'),
(163, 'Teo Badminton Court', 'Pahang', '1630'),
(164, 'Smash 8 Megasmash Badminton Court', 'Pahang', '1640'),
(165, 'LCS Sport Arena', 'Pahang', '1650'),
(166, 'Dewan Badminton Rahazqim', 'Pahang', '1660'),
(167, 'Dewan Badminton Planet Sungai Isap', 'Pahang', '1670'),
(168, 'Kempadang Futsal Center', 'Pahang', '1680'),
(169, 'Legend Futsal Indera Mahkota', 'Pahang', '1690'),
(170, 'De Stadium Futsal KB', 'Kelantan', '1700'),
(171, 'Futsal Harraz Tok Bali', 'Kelantan', '1710'),
(172, 'JPS Futsal', 'Kelantan', '1720'),
(173, 'Afda Futsal Lubok Jong', 'Kelantan', '1730'),
(174, 'Kuyo Futsal', 'Kelantan', '1740'),
(175, 'Prosport Futsal', 'Kelantan', '1750'),
(176, 'Bilal Sport', 'Kelantan', '1760'),
(177, 'Al-Khulafa Sport Center', 'Kelantan', '1770'),
(178, 'JKR Badminton Court', 'Kelantan', '1780'),
(179, 'All Sports Badminton Court', 'Kelantan', '1790'),
(180, 'Pro Seven Futsal Jalan Bayam', 'Kelantan', '1800'),
(181, 'Kota Bharu Badminton Center KBBC 1', 'Kelantan', '1810'),
(182, 'Proseven Futsal Center', 'Kelantan', '1820'),
(183, 'Badminton Association Of Kelantan Hall', 'Kelantan', '1830'),
(184, 'Dewan Badminton Tunjong', 'Kelantan', '1840'),
(185, 'Orbit De Futsal', 'Kelantan', '1850'),
(186, 'Dewan Badminton HRBC', 'Kelantan', '1860'),
(187, 'i5 Badminton Court', 'Kelantan', '1870'),
(188, 'Dewan Dato\' Ibrahim Futsal dan Badminton Court', 'Kelantan', '1880'),
(189, 'BK Badminton Court', 'Kelantan', '1890'),
(190, 'Dewan Badminton AB Green Hall', 'Kelantan', '1900'),
(191, 'Dewan badminton MY morak', 'Kelantan', '1910'),
(192, 'Dewan Dato Lundang B', 'Kelantan', '1920'),
(193, 'Haslina Badminton Hall', 'Kelantan', '1930'),
(194, 'Kompleks Sukan dan Komuniti Besut', 'Terengganu', '1940'),
(195, 'Kompleks Sukan dan Komuniti Besut Jertih', 'Terengganu', '1950'),
(196, 'Kompleks MSN Dungun', 'Terengganu', '1960'),
(197, 'Iltizam Sport Center', 'Terengganu', '1970'),
(198, 'XZone Futsal Center', 'Terengganu', '1980'),
(199, 'Fantasy Futsal Sport', 'Terengganu', '1990'),
(200, 'Miya Futsal Sport Centre', 'Terengganu', '2000'),
(201, 'Sports PC', 'Terengganu', '2010'),
(202, 'DS Sport Centre', 'Terengganu', '2020'),
(203, 'Hazlan Futsal & Indoor Soccer', 'Terengganu', '2030'),
(204, 'Xtreme Futsal Pulau Kambing', 'Terengganu', '2040'),
(205, 'Millipede Futsal Enterprise', 'Terengganu', '2050'),
(206, 'QD de Futsal', 'Terengganu', '2060'),
(207, 'Court Badminton Gong Pok Jin', 'Terengganu', '2070'),
(208, 'Dewan Badminton Dato\' Dr. Mohd Sulaiman', 'Terengganu', '2080'),
(209, 'Dewan Badminton Seri Nilam', 'Terengganu', '2090'),
(210, 'Maecon Sport Centre', 'Terengganu', '2100'),
(211, 'BBBM Badminton Court', 'Terengganu', '2110'),
(212, 'Kompleks Sukan Bukit Kiara', 'Kuala Lumpur', '2120'),
(213, 'Kompleks Sukan Setiawangsa', 'Kuala Lumpur', '2130'),
(214, 'Kompleks Sukan Jalan Duta', 'Kuala Lumpur', '2140'),
(215, 'Kompleks MSN Jalan Raja Muda (SJRM)', 'Kuala Lumpur', '2150'),
(216, 'KOMBES KL', 'Kuala Lumpur', '2160'),
(217, 'Kompleks Sukan Kampong Pandan', 'Kuala Lumpur', '2170'),
(218, 'Mini Stadium Taman Pancarona', 'Kuala Lumpur', '2180'),
(219, 'Lavana Sports Centre', 'Kuala Lumpur', '2190'),
(220, 'Kompleks Sukan Bangsar', 'Kuala Lumpur', '2200'),
(221, 'CK Sports Centre', 'Kuala Lumpur', '2210'),
(222, 'Pusat Sukan Desa Petaling', 'Kuala Lumpur', '2220'),
(223, 'Ace Sports World', 'Kuala Lumpur', '2230'),
(224, 'Sports Arena Sentosa', 'Kuala Lumpur', '2240'),
(225, 'SLK Badminton Centre', 'Kuala Lumpur', '2250'),
(226, 'Forum Pudu', 'Kuala Lumpur', '2260'),
(227, 'Matrik Shuttle Court', 'Kuala Lumpur', '2270'),
(228, 'KSL Futsal Sport Centre', 'Kuala Lumpur', '2280'),
(229, 'Sports Centre Wangsa Maju Section 5', 'Kuala Lumpur', '2290'),
(230, 'Younique Sports Pudu Plaza', 'Kuala Lumpur', '2300'),
(231, 'Bubble Sports Complex Cheras', 'Kuala Lumpur', '2310'),
(232, 'Centre Mart Futsal Centre', 'Kuala Lumpur', '2320'),
(233, 'OUG Shuttle Bug Sports Center', 'Kuala Lumpur', '2330'),
(234, 'KAS Kepong Arena Sports', 'Kuala Lumpur', '2340'),
(235, 'Sport Seven Futsal Centre', 'Kuala Lumpur', '2350'),
(236, 'Pro One Badminton Centre', 'Kuala Lumpur', '2360'),
(237, 'Setapak Badminton Centre', 'Kuala Lumpur', '2370'),
(238, 'Shuttle Bug Badminton Hall', 'Kuala Lumpur', '2380'),
(239, 'Starplus Badminton Centre', 'Kuala Lumpur', '2390'),
(240, 'IOI Sports Centre', 'Kuala Lumpur', '2400'),
(241, 'Avenger Sports Arena', 'Kuala Lumpur', '2410'),
(242, 'Kompleks Sukan Negara Shah Alam(Panasonic)', 'Selangor', '2420'),
(243, 'Frenzy Sports Arena', 'Selangor', '2430'),
(244, 'Kompleks Arena Petaling Jaya', 'Selangor', '2440'),
(245, 'Michael\'s Badminton Academy', 'Selangor', '2450'),
(246, 'Ksl Sport Center Gombak', 'Selangor', '2460'),
(247, 'Real Sports Arena', 'Selangor', '2470'),
(248, 'Athlon De Futsal', 'Selangor', '2480'),
(249, 'DMS Sports Centre', 'Selangor', '2490'),
(250, 'Semenyih Sports Centre', 'Selangor', '2500'),
(251, 'The Challenger Sports Centre PJ', 'Selangor', '2510'),
(252, '222 Sports Centre PJ', 'Selangor', '2520'),
(253, 'Zelka Sports Centre', 'Selangor', '2530'),
(254, 'Forum 19', 'Selangor', '2540'),
(255, 'Central Park Dataran Sunway', 'Selangor', '2550'),
(256, 'Sportizza Badminton Balakong', 'Selangor', '2560'),
(257, 'RKS Sports Centre', 'Selangor', '2570'),
(258, 'White Fairy Futsal & Badminton Court', 'Selangor', '2580'),
(259, 'NPNG Sports Centre', 'Selangor', '2590'),
(260, 'Brothers Futsal Centre', 'Selangor', '2600'),
(261, 'Uptown Sports', 'Selangor', '2610'),
(262, 'Sport Centre 88', 'Selangor', '2620'),
(263, 'Sport 100 Badminton Center', 'Selangor', '2630'),
(264, 'TJH Sport Centre', 'Selangor', '2640'),
(265, 'CK Sports Centre', 'Selangor', '2650'),
(266, 'Puchong Sport Center', 'Selangor', '2660'),
(267, 'KSL Sports Puchong', 'Selangor', '2670'),
(268, 'U One Sport Centre', 'Selangor', '2680'),
(269, 'Sports Garage', 'Selangor', '2690'),
(270, 'Elements Badminton Court', 'Selangor', '2700'),
(271, 'Sport Heroes', 'Selangor', '2710'),
(272, '89 Arena Klang', 'Selangor', '2720'),
(273, 'Kingsport Centre Miri', 'Sarawak', '2730'),
(274, 'Sentosa Sports Centre', 'Sarawak', '2740'),
(275, 'Arena Sukan', 'Sarawak', '2750'),
(276, 'Winner Court', 'Sarawak', '2760'),
(277, 'Tun Tuanku Haji Bujang Arena', 'Sarawak', '2770'),
(278, 'B & G Sport Centre', 'Sarawak', '2780'),
(279, 'Star Sports Complex Sdn Bhd', 'Sarawak', '2790'),
(280, 'Super Sport Arena Samarahan', 'Sarawak', '2800'),
(281, 'Tung Sports Badminton Hall', 'Sarawak', '2810'),
(282, 'TN SPORTS', 'Sarawak', '2820'),
(283, 'Kenyalang Futsal Excellence Centre Bintulu', 'Sarawak', '2830'),
(284, 'Dewan Badminton Stapok', 'Sarawak', '2840'),
(285, 'Champion Futsal Court', 'Sarawak', '2850'),
(286, 'Saturn Futsal', 'Sarawak', '2860'),
(287, 'Infinity Sports Arena', 'Sabah', '2870'),
(288, 'OJS Centre', 'Sabah', '2880'),
(289, 'Dynason Badminton Court', 'Sabah', '2890'),
(290, 'Olympia Badminton Arena', 'Sabah', '2900'),
(291, 'ii sports centre', 'Sabah', '2910'),
(292, 'AI Legacy Badminton Centre', 'Sabah', '2920'),
(293, 'Borneo Sports Arena', 'Sabah', '2930'),
(294, 'Yayasan Sabah Badminton Court', 'Sabah', '2940'),
(295, 'Juara Badminton Arena', 'Sabah', '2950'),
(296, 'My Futsal Club', 'Sabah', '2960'),
(297, 'UTC Sabah Futsal Court', 'Sabah', '2970'),
(298, 'Futsal Yayasan Sabah', 'Sabah', '2980'),
(299, 'One Sports Badminton Tawau', 'Sabah', '2990'),
(300, 'Juara Futsal Arena', 'Sabah', '3000');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `location` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `email`, `password`, `location`) VALUES
(1, 'fit3', 'ahmad.fitri1110@gmail.com', '1112', 'Kelantan'),
(2, 'faris16', 'faris.1600@gmail.com', '1600', 'Selangor'),
(3, 'fitrizul1112', 'ahmad.fitri1112@gmail.com', '11102000', 'Melaka'),
(4, 'fauzan11', 'ahmad.fauzan11@gmail.com', '1110', 'Perak'),
(5, 'irfan3', 'irfan.3020@gmail.com', '3020', 'Johor'),
(6, 'hakim4', 'hakim.40@gmail.com', '4040', 'Terengganu'),
(7, 'anis23', 'anis.2300@gmail.com', '2300', 'Kuala Lumpur'),
(8, 'fit4', 'ahmad.fitri2000@gmail.com', '20001', 'Pulau Pinang'),
(9, 'syauqi08', 'syauqi.fauzi08@gmail.com', '0808', 'Kuala Lumpur'),
(10, 'shahrul01', 'shahrul.fitri01@gmail.com', '0101', 'Perak'),
(11, 'kasim03', 'kasim.bakar03@gmail.com', '0303', 'Kedah'),
(12, 'afifi09', 'afifi09@gmail.com', '0909', 'Melaka'),
(13, 'hazim', 'hazim.03@gmail.com', '0303', 'Negeri Sembilan'),
(14, 'Azlin', 'azlin03@gmail.com', '0303', 'Perak'),
(15, 'FYK', 'muhamad.afiq107@gmail.com', 'rB1610000', 'Melaka'),
(16, 'sharifah', 'sharifah@gmail.com', '0505', 'Kuala Lumpur'),
(17, 'daniel', 'daniel#@email', 'daniel', 'Melaka');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bookingcourt`
--
ALTER TABLE `bookingcourt`
  ADD PRIMARY KEY (`order_id`);

--
-- Indexes for table `staff`
--
ALTER TABLE `staff`
  ADD PRIMARY KEY (`staff_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `bookingcourt`
--
ALTER TABLE `bookingcourt`
  MODIFY `order_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=66;

--
-- AUTO_INCREMENT for table `staff`
--
ALTER TABLE `staff`
  MODIFY `staff_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=301;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
