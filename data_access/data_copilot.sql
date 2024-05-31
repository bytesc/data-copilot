/*
 Navicat Premium Data Transfer

 Source Server         : mysql
 Source Server Type    : MySQL
 Source Server Version : 80031
 Source Host           : localhost:3306
 Source Schema         : data_copilot

 Target Server Type    : MySQL
 Target Server Version : 80031
 File Encoding         : 65001

 Date: 31/05/2024 18:27:48
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for 员工
-- ----------------------------
DROP TABLE IF EXISTS `员工`;
CREATE TABLE `员工`  (
  `员工号` int NOT NULL,
  `姓名` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `部门` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`员工号`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 员工
-- ----------------------------
INSERT INTO `员工` VALUES (1, 'John', 'HR');
INSERT INTO `员工` VALUES (2, 'Emma', 'Sales');
INSERT INTO `员工` VALUES (3, 'Liam', 'IT');
INSERT INTO `员工` VALUES (4, 'Olivia', 'Marketing');
INSERT INTO `员工` VALUES (5, 'William', 'Finance');

-- ----------------------------
-- Table structure for 工资
-- ----------------------------
DROP TABLE IF EXISTS `工资`;
CREATE TABLE `工资`  (
  `员工号` int NOT NULL,
  `工资` int NULL DEFAULT NULL,
  PRIMARY KEY (`员工号`) USING BTREE,
  CONSTRAINT `工资_ibfk_1` FOREIGN KEY (`员工号`) REFERENCES `员工` (`员工号`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 工资
-- ----------------------------
INSERT INTO `工资` VALUES (1, 5000);
INSERT INTO `工资` VALUES (2, 6000);
INSERT INTO `工资` VALUES (3, 4500);
INSERT INTO `工资` VALUES (4, 7000);
INSERT INTO `工资` VALUES (5, 5500);

-- ----------------------------
-- Table structure for 销售数据
-- ----------------------------
DROP TABLE IF EXISTS `销售数据`;
CREATE TABLE `销售数据`  (
  `国家` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `销量` int NULL DEFAULT NULL,
  `进行订单` int NULL DEFAULT NULL,
  `结束订单` int NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 销售数据
-- ----------------------------
INSERT INTO `销售数据` VALUES ('美国', 5000, 142, 120);
INSERT INTO `销售数据` VALUES ('英国', 3200, 80, 70);
INSERT INTO `销售数据` VALUES ('法国', 2900, 70, 60);
INSERT INTO `销售数据` VALUES ('德国', 4100, 90, 80);
INSERT INTO `销售数据` VALUES ('意大利', 2300, 60, 50);
INSERT INTO `销售数据` VALUES ('西班牙', 2100, 50, 40);
INSERT INTO `销售数据` VALUES ('加拿大', 2500, 40, 30);
INSERT INTO `销售数据` VALUES ('澳大利亚', 2600, 30, 20);
INSERT INTO `销售数据` VALUES ('日本', 4500, 110, 100);
INSERT INTO `销售数据` VALUES ('中国', 7000, 120, 110);

SET FOREIGN_KEY_CHECKS = 1;
