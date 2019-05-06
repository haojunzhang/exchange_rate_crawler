# Automatically created by: scrapydweb x scrapyd-client

from setuptools import setup, find_packages

setup(
    name         = 'project',
    version      = '1.0',
    packages     = find_packages(),
    entry_points = {'scrapy': ['settings = exchange_rate_scrapy.settings']},
)
