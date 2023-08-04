# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE OR REPLACE TEMPORARY VIEW hola_mundo AS
# MAGIC SELECT 'Hola, mundo' AS mensaje;
# MAGIC
# MAGIC SELECT mensaje FROM hola_mundo;
