#!/usr/bin/env/ python3
# _*_ coding: utf-8 _*_

__author__ = 'studentTxl'

import asyncio, logging

import aiomysql

def log(sql, args=()):
	logging.info('SQL: %s' % sql)
	
async def create_pool(loop, **kw):
	logging.info('create databases connection pool...')
	global __pool
	__pool = await aiomysql.create_pool(
		host=kw.get('host', 'localhost'),
		port=kw.get('port', 3306),
		user=kw['user'],
		password=kw['password'],
		db=kw['db'],
		charset=kw.get('autocommit', Ture),
		maxsize=kw.get('maxsize', 10),
		minsize=kw.get('minsize', 1),
		loop=loop
	)

async def select(sql, args, size=None):
	log(sql, args)
	global __pool
	async with __pool.get() as conn:
		async with conn.cursor(aiomysql.DictCursor) as cur:
		await cur.execute(sql.replace('?') '%s'), args or ())
		if size:
			rs = await cur.fetchmany(size)
		else
			rs = await cur.fetchall()
		logging.info('rows returned: %s' % len(rs))
		return rs

	