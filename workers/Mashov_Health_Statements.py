# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from datetime import date, time, datetime
from selenium.common.exceptions import InvalidSessionIdException
import os, time, helpers
from loguru import logger


def sign(user, password, schoolid, kidnum, Image):
    try:
        browser = helpers.GetBrowser()
        logger.info("Starting process")

        try:
            helpers.ping(browser, 'mashov')
        except:
            logger.debug('Unable to ping')
        logger.debug('----------------------------------------------------------------------')
        logger.info("Starting Mashov Sign process for kid number: " + kidnum)
        
        browser.get("https://web.mashov.info/students/login")
        time.sleep(3)
              
        #choose school:
        form_element_mashov_select_school = browser.find_element_by_xpath("//*[@id='mat-input-3']")
        form_element_mashov_user = browser.find_element_by_xpath("//*[@id='mat-input-0']")
        form_element_mashov_password = browser.find_element_by_xpath("//*[@id='mat-input-4']")
        form_element_mashov_login = browser.find_element_by_xpath("//*[@id='mat-tab-content-0-0']/div/div/button[1]")


        form_element_mashov_select_school.click()
        form_element_mashov_select_school.send_keys(schoolid)
        form_element_mashov_select_school.send_keys(Keys.ARROW_DOWN)
        form_element_mashov_select_school.send_keys(Keys.RETURN)

        form_element_mashov_user.click()
        form_element_mashov_user.send_keys(user)
        form_element_mashov_password.click()
        form_element_mashov_password.send_keys(password)
        form_element_mashov_login.click()
        time.sleep(3)

        logger.info(f"Logged in") 

        form_element_mashov_select_daily_corona_report = browser.find_element_by_xpath("/html/body/mshv-root/mshv-main/mat-sidenav-container/mat-sidenav-content/mshv-student-covidsplash/mat-card/mat-card-content/div[3]/mat-card")
        form_element_mashov_select_daily_corona_report.click()
        time.sleep(2)

        form_element_mashov_submit_report = browser.find_element_by_xpath("/html/body/mshv-root/mshv-main/mat-sidenav-container/mat-sidenav-content/mshv-students-covid-clearance/mat-card/mat-card/mat-card-content[2]/mat-card-actions/button")
        if 'אני מצהיר' in form_element_mashov_submit_report.text:
            form_element_mashov_submit_report.click()


        logger.info(f"Submitted Report")
        time.sleep(1) 

        helpers.log_browser(browser)
        helpers.fullpage_screenshot(browser,Image)        
        
        logger.info(f"Screenshot Saved")
        logger.info("Finished Mashov Sign process for kid number: " + kidnum)
        logger.debug('----------------------------------------------------------------------')        
        
        return 1
    except Exception as ex:
        logger.error(str(ex))
        return 0



