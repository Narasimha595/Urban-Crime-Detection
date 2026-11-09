-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jan 30, 2025 at 01:18 PM
-- Server version: 8.3.0
-- PHP Version: 8.2.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `crime_detection`
--
CREATE DATABASE IF NOT EXISTS `crime_detection` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `crime_detection`;

-- --------------------------------------------------------

--
-- Table structure for table `ada_algo`
--

DROP TABLE IF EXISTS `ada_algo`;
CREATE TABLE IF NOT EXISTS `ada_algo` (
  `Ada_ID` int NOT NULL AUTO_INCREMENT,
  `Accuracy` longtext NOT NULL,
  `Precession` longtext NOT NULL,
  `F1_Score` longtext NOT NULL,
  `Recall` longtext NOT NULL,
  `Name` longtext NOT NULL,
  PRIMARY KEY (`Ada_ID`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `ada_algo`
--

INSERT INTO `ada_algo` (`Ada_ID`, `Accuracy`, `Precession`, `F1_Score`, `Recall`, `Name`) VALUES
(2, '55.88', '40.89', '36.18', '41.32', 'Ada Boost Algorithm');

-- --------------------------------------------------------

--
-- Table structure for table `all_users`
--

DROP TABLE IF EXISTS `all_users`;
CREATE TABLE IF NOT EXISTS `all_users` (
  `User_id` int NOT NULL AUTO_INCREMENT,
  `user_Profile` varchar(100) NOT NULL,
  `User_Email` varchar(50) NOT NULL,
  `User_Status` varchar(10) NOT NULL,
  PRIMARY KEY (`User_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `ann_algo`
--

DROP TABLE IF EXISTS `ann_algo`;
CREATE TABLE IF NOT EXISTS `ann_algo` (
  `Ann_ID` int NOT NULL AUTO_INCREMENT,
  `Accuracy` longtext NOT NULL,
  `Precession` longtext NOT NULL,
  `F1_Score` longtext NOT NULL,
  `Recall` longtext NOT NULL,
  `Name` longtext NOT NULL,
  PRIMARY KEY (`Ann_ID`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `ann_algo`
--

INSERT INTO `ann_algo` (`Ann_ID`, `Accuracy`, `Precession`, `F1_Score`, `Recall`, `Name`) VALUES
(6, '8.98', '1.5', '2.75', '16.67', 'ANN Algorithm');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=89 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add ada_algo', 7, 'add_ada_algo'),
(26, 'Can change ada_algo', 7, 'change_ada_algo'),
(27, 'Can delete ada_algo', 7, 'delete_ada_algo'),
(28, 'Can view ada_algo', 7, 'view_ada_algo'),
(29, 'Can add all_users_model', 8, 'add_all_users_model'),
(30, 'Can change all_users_model', 8, 'change_all_users_model'),
(31, 'Can delete all_users_model', 8, 'delete_all_users_model'),
(32, 'Can view all_users_model', 8, 'view_all_users_model'),
(33, 'Can add ann_algo', 9, 'add_ann_algo'),
(34, 'Can change ann_algo', 9, 'change_ann_algo'),
(35, 'Can delete ann_algo', 9, 'delete_ann_algo'),
(36, 'Can view ann_algo', 9, 'view_ann_algo'),
(37, 'Can add dataset', 10, 'add_dataset'),
(38, 'Can change dataset', 10, 'change_dataset'),
(39, 'Can delete dataset', 10, 'delete_dataset'),
(40, 'Can view dataset', 10, 'view_dataset'),
(41, 'Can add d t_algo', 11, 'add_dt_algo'),
(42, 'Can change d t_algo', 11, 'change_dt_algo'),
(43, 'Can delete d t_algo', 11, 'delete_dt_algo'),
(44, 'Can view d t_algo', 11, 'view_dt_algo'),
(45, 'Can add lightgbm_algo', 12, 'add_lightgbm_algo'),
(46, 'Can change lightgbm_algo', 12, 'change_lightgbm_algo'),
(47, 'Can delete lightgbm_algo', 12, 'delete_lightgbm_algo'),
(48, 'Can view lightgbm_algo', 12, 'view_lightgbm_algo'),
(49, 'Can add logistic', 13, 'add_logistic'),
(50, 'Can change logistic', 13, 'change_logistic'),
(51, 'Can delete logistic', 13, 'delete_logistic'),
(52, 'Can view logistic', 13, 'view_logistic'),
(53, 'Can add Adaptive Region Partitioning (ARP)', 14, 'add_randomforest'),
(54, 'Can change Adaptive Region Partitioning (ARP)', 14, 'change_randomforest'),
(55, 'Can delete Adaptive Region Partitioning (ARP)', 14, 'delete_randomforest'),
(56, 'Can view Adaptive Region Partitioning (ARP)', 14, 'view_randomforest'),
(57, 'Can add upload_dataset_model', 15, 'add_upload_dataset_model'),
(58, 'Can change upload_dataset_model', 15, 'change_upload_dataset_model'),
(59, 'Can delete upload_dataset_model', 15, 'delete_upload_dataset_model'),
(60, 'Can view upload_dataset_model', 15, 'view_upload_dataset_model'),
(61, 'Can add contact_ model', 16, 'add_contact_model'),
(62, 'Can change contact_ model', 16, 'change_contact_model'),
(63, 'Can delete contact_ model', 16, 'delete_contact_model'),
(64, 'Can view contact_ model', 16, 'view_contact_model'),
(65, 'Can add dataset_ model', 17, 'add_dataset_model'),
(66, 'Can change dataset_ model', 17, 'change_dataset_model'),
(67, 'Can delete dataset_ model', 17, 'delete_dataset_model'),
(68, 'Can view dataset_ model', 17, 'view_dataset_model'),
(69, 'Can add last_login', 18, 'add_last_login'),
(70, 'Can change last_login', 18, 'change_last_login'),
(71, 'Can delete last_login', 18, 'delete_last_login'),
(72, 'Can view last_login', 18, 'view_last_login'),
(73, 'Can add predict_ model', 19, 'add_predict_model'),
(74, 'Can change predict_ model', 19, 'change_predict_model'),
(75, 'Can delete predict_ model', 19, 'delete_predict_model'),
(76, 'Can view predict_ model', 19, 'view_predict_model'),
(77, 'Can add user_ model', 20, 'add_user_model'),
(78, 'Can change user_ model', 20, 'change_user_model'),
(79, 'Can delete user_ model', 20, 'delete_user_model'),
(80, 'Can view user_ model', 20, 'view_user_model'),
(81, 'Can add data_set', 21, 'add_data_set'),
(82, 'Can change data_set', 21, 'change_data_set'),
(83, 'Can delete data_set', 21, 'delete_data_set'),
(84, 'Can view data_set', 21, 'view_data_set'),
(85, 'Can add feedback', 22, 'add_feedback'),
(86, 'Can change feedback', 22, 'change_feedback'),
(87, 'Can delete feedback', 22, 'delete_feedback'),
(88, 'Can view feedback', 22, 'view_feedback');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `contact`
--

DROP TABLE IF EXISTS `contact`;
CREATE TABLE IF NOT EXISTS `contact` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `yourname` varchar(50) NOT NULL,
  `youremail` varchar(254) NOT NULL,
  `phone` longtext NOT NULL,
  `Message` longtext,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `dataset`
--

DROP TABLE IF EXISTS `dataset`;
CREATE TABLE IF NOT EXISTS `dataset` (
  `DS_ID` int NOT NULL AUTO_INCREMENT,
  `Age` int NOT NULL,
  `Glucose` int NOT NULL,
  `BloodPressure` int NOT NULL,
  `SkinThickness` int NOT NULL,
  `Insulin` int NOT NULL,
  `BMI` int NOT NULL,
  `DiabetesPedigreeFunction` int NOT NULL,
  `Pregnancies` int NOT NULL,
  PRIMARY KEY (`DS_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'permission'),
(3, 'auth', 'group'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(7, 'adminapp', 'ada_algo'),
(8, 'adminapp', 'all_users_model'),
(9, 'adminapp', 'ann_algo'),
(10, 'adminapp', 'dataset'),
(11, 'adminapp', 'dt_algo'),
(12, 'adminapp', 'lightgbm_algo'),
(13, 'adminapp', 'logistic'),
(14, 'adminapp', 'randomforest'),
(15, 'adminapp', 'upload_dataset_model'),
(16, 'mainapp', 'contact_model'),
(17, 'mainapp', 'dataset_model'),
(18, 'mainapp', 'last_login'),
(19, 'mainapp', 'predict_model'),
(20, 'mainapp', 'user_model'),
(21, 'userapp', 'data_set'),
(22, 'userapp', 'feedback');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2025-01-30 09:00:27.730913'),
(2, 'auth', '0001_initial', '2025-01-30 09:00:28.162939'),
(3, 'admin', '0001_initial', '2025-01-30 09:00:28.305555'),
(4, 'admin', '0002_logentry_remove_auto_add', '2025-01-30 09:00:28.311539'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2025-01-30 09:00:28.317557'),
(6, 'adminapp', '0001_initial', '2025-01-30 09:00:28.388124'),
(7, 'contenttypes', '0002_remove_content_type_name', '2025-01-30 09:00:28.453243'),
(8, 'auth', '0002_alter_permission_name_max_length', '2025-01-30 09:00:28.482850'),
(9, 'auth', '0003_alter_user_email_max_length', '2025-01-30 09:00:28.523854'),
(10, 'auth', '0004_alter_user_username_opts', '2025-01-30 09:00:28.529838'),
(11, 'auth', '0005_alter_user_last_login_null', '2025-01-30 09:00:28.560755'),
(12, 'auth', '0006_require_contenttypes_0002', '2025-01-30 09:00:28.562750'),
(13, 'auth', '0007_alter_validators_add_error_messages', '2025-01-30 09:00:28.568733'),
(14, 'auth', '0008_alter_user_username_max_length', '2025-01-30 09:00:28.610606'),
(15, 'auth', '0009_alter_user_last_name_max_length', '2025-01-30 09:00:28.646063'),
(16, 'auth', '0010_alter_group_name_max_length', '2025-01-30 09:00:28.675984'),
(17, 'auth', '0011_update_proxy_permissions', '2025-01-30 09:00:28.687953'),
(18, 'auth', '0012_alter_user_first_name_max_length', '2025-01-30 09:00:28.723852'),
(19, 'mainapp', '0001_initial', '2025-01-30 09:00:28.759720'),
(20, 'sessions', '0001_initial', '2025-01-30 09:00:28.790635'),
(21, 'userapp', '0001_initial', '2025-01-30 09:00:28.855470');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('znpjpp723kbnvcqx64xna3e994elbt39', 'eyJlbWFpbCI6InVzZXJAZ21haWwuY29tIiwidXNlcl9pZCI6MX0:1tdQjG:gwE2yGGJkZN1ey9bEDJWtyxON5EmW8VHhMu2zoy_XYo', '2025-02-13 09:20:54.131300'),
('uzy9qg71nuhh6ipvyospndh3pttordep', 'eyJ1c2VyX2lkIjoxLCJwcmVkaWN0aW9uX3Jlc3VsdCI6MX0:1tdTw7:Q4XV8lIdzpsYgbalMny_h94fAZjGU6PEqOV8ejU7At4', '2025-02-13 12:46:23.745915');

-- --------------------------------------------------------

--
-- Table structure for table `dt_algo`
--

DROP TABLE IF EXISTS `dt_algo`;
CREATE TABLE IF NOT EXISTS `dt_algo` (
  `DT_ID` int NOT NULL AUTO_INCREMENT,
  `Accuracy` longtext NOT NULL,
  `Precession` longtext NOT NULL,
  `F1_Score` longtext NOT NULL,
  `Recall` longtext NOT NULL,
  `Name` longtext NOT NULL,
  PRIMARY KEY (`DT_ID`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `dt_algo`
--

INSERT INTO `dt_algo` (`DT_ID`, `Accuracy`, `Precession`, `F1_Score`, `Recall`, `Name`) VALUES
(5, '99.99', '100.0', '100.0', '99.99', 'Decision Tree Algorithm (Train)');

-- --------------------------------------------------------

--
-- Table structure for table `feedback_details`
--

DROP TABLE IF EXISTS `feedback_details`;
CREATE TABLE IF NOT EXISTS `feedback_details` (
  `feed_id` int NOT NULL AUTO_INCREMENT,
  `rating` varchar(100) DEFAULT NULL,
  `review` varchar(225) DEFAULT NULL,
  `sentiment` varchar(100) DEFAULT NULL,
  `datetime` datetime(6) NOT NULL,
  `reviewer_id` int DEFAULT NULL,
  PRIMARY KEY (`feed_id`),
  KEY `feedback_details_reviewer_id_fc389009` (`reviewer_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `last_login`
--

DROP TABLE IF EXISTS `last_login`;
CREATE TABLE IF NOT EXISTS `last_login` (
  `Id` int NOT NULL AUTO_INCREMENT,
  `Login_Time` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `lightgbm_algo`
--

DROP TABLE IF EXISTS `lightgbm_algo`;
CREATE TABLE IF NOT EXISTS `lightgbm_algo` (
  `Lightgbm_ID` int NOT NULL AUTO_INCREMENT,
  `Accuracy` longtext NOT NULL,
  `Precession` longtext NOT NULL,
  `F1_Score` longtext NOT NULL,
  `Recall` longtext NOT NULL,
  `Name` longtext NOT NULL,
  PRIMARY KEY (`Lightgbm_ID`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `lightgbm_algo`
--

INSERT INTO `lightgbm_algo` (`Lightgbm_ID`, `Accuracy`, `Precession`, `F1_Score`, `Recall`, `Name`) VALUES
(2, '71.58', '43.0', '46.56', '55.68', 'Lightgbm Boost Algorithm');

-- --------------------------------------------------------

--
-- Table structure for table `logistic`
--

DROP TABLE IF EXISTS `logistic`;
CREATE TABLE IF NOT EXISTS `logistic` (
  `Logistic_ID` int NOT NULL AUTO_INCREMENT,
  `Accuracy` longtext NOT NULL,
  `Precession` longtext NOT NULL,
  `F1_Score` longtext NOT NULL,
  `Recall` longtext NOT NULL,
  `Name` longtext NOT NULL,
  PRIMARY KEY (`Logistic_ID`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `logistic`
--

INSERT INTO `logistic` (`Logistic_ID`, `Accuracy`, `Precession`, `F1_Score`, `Recall`, `Name`) VALUES
(3, '57.63', '17.55', '24.08', '24.08', 'Logistic Algorithm');

-- --------------------------------------------------------

--
-- Table structure for table `predict_detail`
--

DROP TABLE IF EXISTS `predict_detail`;
CREATE TABLE IF NOT EXISTS `predict_detail` (
  `predict_id` int NOT NULL AUTO_INCREMENT,
  `Field_1` varchar(60) DEFAULT NULL,
  `Field_2` varchar(60) DEFAULT NULL,
  `Field_3` varchar(60) DEFAULT NULL,
  `Field_4` varchar(60) DEFAULT NULL,
  `Field_5` varchar(60) DEFAULT NULL,
  `Field_6` varchar(60) DEFAULT NULL,
  `Field_7` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`predict_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `randomforest`
--

DROP TABLE IF EXISTS `randomforest`;
CREATE TABLE IF NOT EXISTS `randomforest` (
  `Random_ID` int NOT NULL AUTO_INCREMENT,
  `Accuracy` longtext NOT NULL,
  `Precession` longtext NOT NULL,
  `F1_Score` longtext NOT NULL,
  `Recall` longtext NOT NULL,
  `Name` longtext NOT NULL,
  PRIMARY KEY (`Random_ID`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `randomforest`
--

INSERT INTO `randomforest` (`Random_ID`, `Accuracy`, `Precession`, `F1_Score`, `Recall`, `Name`) VALUES
(4, '71.08', '41.63', '56.68', '56.68', 'Adaptive Region Partitioning (ARP) Algorithm');

-- --------------------------------------------------------

--
-- Table structure for table `upload`
--

DROP TABLE IF EXISTS `upload`;
CREATE TABLE IF NOT EXISTS `upload` (
  `Data_id` int NOT NULL AUTO_INCREMENT,
  `Image` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Data_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `upload_dataset`
--

DROP TABLE IF EXISTS `upload_dataset`;
CREATE TABLE IF NOT EXISTS `upload_dataset` (
  `User_id` int NOT NULL AUTO_INCREMENT,
  `Dataset` varchar(100) DEFAULT NULL,
  `File_size` varchar(100) NOT NULL,
  `Date_Time` datetime(6) NOT NULL,
  PRIMARY KEY (`User_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `upload_dataset`
--

INSERT INTO `upload_dataset` (`User_id`, `Dataset`, `File_size`, `Date_Time`) VALUES
(1, 'crime_cleaned_data.csv', '1253.919921875 kb', '2025-01-30 10:36:14.881589');

-- --------------------------------------------------------

--
-- Table structure for table `upload_user`
--

DROP TABLE IF EXISTS `upload_user`;
CREATE TABLE IF NOT EXISTS `upload_user` (
  `Data_id` int NOT NULL AUTO_INCREMENT,
  `Image` varchar(100) NOT NULL,
  PRIMARY KEY (`Data_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
CREATE TABLE IF NOT EXISTS `user` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `fullname` varchar(50) NOT NULL,
  `password` longtext NOT NULL,
  `email` varchar(254) NOT NULL,
  `age` int DEFAULT NULL,
  `phonenumber` longtext NOT NULL,
  `address` longtext NOT NULL,
  `Image` varchar(100) DEFAULT NULL,
  `datetime` datetime(6) DEFAULT NULL,
  `user_status` longtext,
  `otp` int DEFAULT NULL,
  `otp_status` longtext,
  `Last_Login_Time` time(6) DEFAULT NULL,
  `Last_Login_Date` date DEFAULT NULL,
  `No_Of_Times_Login` int DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`user_id`, `fullname`, `password`, `email`, `age`, `phonenumber`, `address`, `Image`, `datetime`, `user_status`, `otp`, `otp_status`, `Last_Login_Time`, `Last_Login_Date`, `No_Of_Times_Login`) VALUES
(1, 'User', '123', 'user@gmail.com', 23, '48965365365365651', 'Hyd', 'images/detective-story_L8BpQgJ.png', '2025-01-30 12:11:10.670269', 'accepted', 7900, 'verified', '14:50:56.634976', '2025-01-30', 17);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
