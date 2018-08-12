-- phpMyAdmin SQL Dump
-- version 4.4.10
-- http://www.phpmyadmin.net
--
-- Host: localhost:3306
-- Generation Time: Aug 12, 2018 at 02:46 PM
-- Server version: 5.5.42
-- PHP Version: 7.0.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

--
-- Database: `myblog`
--

-- --------------------------------------------------------

--
-- Table structure for table `articles`
--

CREATE TABLE `articles` (
  `id` int(11) NOT NULL,
  `title` varchar(255) COLLATE utf8_turkish_ci NOT NULL,
  `author` varchar(100) COLLATE utf8_turkish_ci NOT NULL,
  `body` text COLLATE utf8_turkish_ci NOT NULL,
  `create_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Dumping data for table `articles`
--

INSERT INTO `articles` (`id`, `title`, `author`, `body`, `create_date`) VALUES
(1, 'Article 1', 'eziz', 'lorem ipsumlar, lorem ipsumlar, lorem ipsumlar, lorem ipsumlar, lorem ipsumlar, lorem ipsumlar, lorem ipsumlar, lorem ipsumlar, lorem ipsumlar, lorem ipsumlar, lorem ipsumlar, lorem ipsumlar, lorem ipsumlar, lorem ipsumlar, lorem ipsumlar, lorem ipsumlar, lorem ipsumlar, lorem ipsumlar, lorem ipsumlar, lorem ipsumlar, lorem ipsumlar, lorem ipsumlar, ', '2018-08-11 14:11:38'),
(2, 'Article two', 'eziz', 'lorem mami, lorem mim,&nbsp;lorem mami, lorem mim,&nbsp;lorem mami, lorem mim,&nbsp;lorem mami, lorem mim,&nbsp;lorem mami, lorem mim,&nbsp;lorem mami, lorem mim,&nbsp;lorem mami, lorem mim,&nbsp;lorem mami, lorem mim,&nbsp;lorem mami, lorem mim,&nbsp;lorem mami, lorem mim,&nbsp;lorem mami, lorem mim,&nbsp;lorem mami, lorem mim,&nbsp;lorem mami, lorem mim,&nbsp;lorem mami, lorem mim,&nbsp;lorem mami, lorem mim,&nbsp;lorem mami, lorem mim,&nbsp;lorem mami, lorem mim,&nbsp;lorem mami, lorem mim,&nbsp;lorem mami, lorem mim,&nbsp;lorem mami, lorem mim!</p><p>&nbsp;</p><p>lorem mami, lorem mim,&nbsp;lorem mami, lorem mim,&nbsp;lorem mami, lorem mim,&nbsp;lorem mami, lorem mim,&nbsp;lorem mami, lorem mim,&nbsp;lorem mami, lorem mim,&nbsp;lorem mami, lorem mim,&nbsp;lorem mami, lorem mim,&nbsp;lorem mami, lorem mim,&nbsp;lorem mami, lorem mim,&nbsp;lorem mami, lorem mim,&nbsp;lorem mami, lorem mim,&nbsp;lorem mami, lorem mim,&nbsp;lorem mami, lorem mim,&nbsp;lorem mami, lorem mim,&nbsp;lorem mami, lorem mim,&nbsp;lorem mami, lorem mim.', '2018-08-11 15:19:08'),
(3, 'Article Three', 'eziz', 'lkjasdlkjasd   asdaslkjdaslkdjas , sdasdas lkjasdlkjasd   asdaslkjdaslkdjas , sdasdas lkjasdlkjasd   asdaslkjdaslkdjas , sdasdas lkjasdlkjasd   asdaslkjdaslkdjas , sdasdas lkjasdlkjasd   asdaslkjdaslkdjas , sdasdas lkjasdlkjasd   asdaslkjdaslkdjas , sdasdas lkjasdlkjasd   asdaslkjdaslkdjas , sdasdas lkjasdlkjasd   asdaslkjdaslkdjas , sdasdas lkjasdlkjasd   asdaslkjdaslkdjas , sdasdas lkjasdlkjasd   asdaslkjdaslkdjas , sdasdas lkjasdlkjasd   asdaslkjdaslkdjas , sdasdas lkjasdlkjasd   asdaslkjdaslkdjas , sdasdas ', '2018-08-11 17:42:50');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `name` varchar(100) COLLATE utf8_turkish_ci NOT NULL,
  `email` varchar(100) COLLATE utf8_turkish_ci NOT NULL,
  `username` varchar(30) COLLATE utf8_turkish_ci NOT NULL,
  `password` varchar(100) COLLATE utf8_turkish_ci NOT NULL,
  `register_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `name`, `email`, `username`, `password`, `register_date`) VALUES
(1, 'eziz', 'eziz@gmail.com', 'eziz', '$5$rounds=535000$.i8k8KPBQKqWzsCB$yJ20ThOplhV0jArp9IECnbq8wpxNYqoNNLuY6Shj774', '2018-08-02 11:05:39');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `articles`
--
ALTER TABLE `articles`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `articles`
--
ALTER TABLE `articles`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=2;