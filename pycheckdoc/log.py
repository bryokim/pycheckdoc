#!/usr/bin/env python3
"""Logging module"""

import logging

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    logging.debug("This is not an error")
    logging.info("This is not an error")
    logging.warning("This is not an error")
    logging.error("This is not an error")
    logging.critical("This is not an error")

    print("")

    logging.basicConfig(level=logging.DEBUG)

    logging.debug("This is not an error")
    logging.info("This is not an error")
    logging.warning("This is not an error")
    logging.error("This is not an error")
    logging.critical("This is not an error")
