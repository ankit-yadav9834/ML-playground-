import logging 


# logging setting

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%y-%m-%d %H:%M:%S',
    handlers= [
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)

logger= logging.getLogger("ArithmaticApp")

def add(a,b):
    result = a+b
    logger.debug(f"Adding {a}+{b} = {result}")
    return result

def subs(a,b):
    result = a-b
    logger.debug(f"Substracting {a}-{b} = {result}")
    return result

def multi(a,b):
    result = a*b
    logger.debug(f"Multiplication {a}*{b} = {result}")
    return result


def divide(a,b):
    try:
        result = a/b
        logger.debug(f"Dividing {a}/{b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero error")
        return None

add(10,15)
subs(115,10)
multi(10,5)
divide(20,10)