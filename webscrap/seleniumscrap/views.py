# Django
from django.conf.urls import url
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
import os
#from rest_framework.views import exception_handler

# Selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import TimeoutException
#from rest_framework.generics import CreateAPIView


url='https://sanctionssearch.ofac.treas.gov/'

driver = webdriver.Chrome(executable_path='C:\\Users\\pimpa\\Downloads\\chromedriver_win32\\chromedriver.exe')





        
def scrapping(driver,url):
    try:
            
        driver.get(url)
        sel = Select(driver.find_element_by_xpath("//select[@name='ctl00$MainContent$ddlType']"))
        sel.select_by_visible_text("Aircraft")
        name_input = driver.find_element_by_xpath("//input[@name='ctl00$MainContent$txtLastName']")
        name_input.send_keys("mehul")
        Id_input = driver.find_element_by_xpath("//input[@name='ctl00$MainContent$txtID']")
        Id_input.send_keys("2254")
        el = driver.find_element_by_id('ctl00_MainContent_lstPrograms')
        for option in el.find_elements_by_tag_name('option'):
            if option.text == 'All':
                option.click()
                break
                
        Address_input = driver.find_element_by_xpath("//input[@name='ctl00$MainContent$txtAddress']")
        Address_input.send_keys("sec-11")
        City_input = driver.find_element_by_xpath("//input[@name='ctl00$MainContent$txtCity']")
        City_input.send_keys("Delhi")
        State_input = driver.find_element_by_xpath("//input[@name='ctl00$MainContent$txtState']")
        State_input.send_keys("Delhi")
        country = Select(driver.find_element_by_xpath("//select[@name='ctl00$MainContent$ddlCountry']"))
        country.select_by_visible_text("India")
        List = Select(driver.find_element_by_xpath("//select[@name='ctl00$MainContent$ddlList']"))
        List.select_by_visible_text("All")
        search_button = driver.find_element_by_xpath(
            ".//*[@type='submit']").click()
                
    except TimeoutException:
        print("Timed out waiting for page to load")
        driver.quit()
            
    driver.get(url)
    data=driver.find_element_by_id('ctl00_MainContent_pnlMessage').text
    print(data)










if __name__ == '__main__':
    scrapping(driver,url)
    