/*
Navicat MySQL Data Transfer

Source Server         : ESG
Source Server Version : 50722
Source Host           : esg.czyh4zihfoly.us-east-2.rds.amazonaws.com:3306
Source Database       : esg

Target Server Type    : MYSQL
Target Server Version : 50722
File Encoding         : 65001

Date: 2020-03-13 22:09:33
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for ESGScore
-- ----------------------------
DROP TABLE IF EXISTS `ESGScore`;
CREATE TABLE `ESGScore` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `Secid` int(255) NOT NULL,
  `AsOfDate` varchar(100) DEFAULT NULL,
  `Symbol` varchar(255) DEFAULT NULL,
  `ESGScoresSocial` varchar(255) DEFAULT NULL,
  `ESGScores_Environmental` varchar(255) DEFAULT NULL,
  `ESGScores_Governance` varchar(255) DEFAULT NULL,
  `ESGScores_Total` varchar(255) DEFAULT NULL,
  `Alcoholic_Beverages` tinyint(2) DEFAULT NULL,
  `Adult_Entertainment` tinyint(2) DEFAULT NULL,
  `Gambling` tinyint(2) DEFAULT NULL,
  `Tobacco_Products` tinyint(2) DEFAULT NULL,
  `Animal_Testing` tinyint(2) DEFAULT NULL,
  `Fur_and_Specialty_Leather` tinyint(2) DEFAULT NULL,
  `Controversial_Weapons` tinyint(2) DEFAULT NULL,
  `Small_Arms` tinyint(2) DEFAULT NULL,
  `Catholic_Values` tinyint(2) DEFAULT NULL,
  `GMO` tinyint(2) DEFAULT NULL,
  `Military_Contracting` tinyint(2) DEFAULT NULL,
  `Pesticides` tinyint(2) DEFAULT NULL,
  `Thermal_Coal` tinyint(2) DEFAULT NULL,
  `Palm_Oil` tinyint(2) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=346 DEFAULT CHARSET=latin1;
