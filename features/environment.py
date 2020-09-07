import logging as logger


def before_all(context):
    logger.info("Before All")


def after_all(context):
    logger.info("After All")


def before_scenario(context, scenario):
    logger.info("Before Scenario", scenario.status.name)


def after_scenario(context, scenario):
    logger.info("After Scenario", scenario.status.name)
    if scenario.status.name == 'failed':
        logger.info("TODO should take screenshot")
    context.browser.close_browser()


def before_step(context, step):
    logger.info("Before Step")


def after_step(context, step):
    logger.info("After Step")
