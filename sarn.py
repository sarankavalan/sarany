#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from selenium import webdriver
from bs4 import BeautifulSoup
import string
import time
from pymongo import MongoClient

import random

from random import randint

import os
import sys
import codecs
import pprint

from selenium.webdriver.chrome.options import Options

from selenium import webdriver

option = webdriver.ChromeOptions()
chrome_prefs = {}
option.experimental_options["prefs"] = chrome_prefs
chrome_prefs["profile.default_content_settings"] = {"images": 2}
chrome_prefs["profile.managed_default_content_settings"] = {"images": 2}



def openfile():
	try:
		print("VPN Injecting..")
		os.startfile('psiphon3.exe')
		time.sleep(9)
	except Exception as e:
		print(e)


def closefile():
	try:
		print("VPN Removed")
		os.system("TASKKILL.exe /IM psiphon3.exe")
		time.sleep(8)
	except Exception as e:
		print(e)
        
def IE():
	try:
		print("IE closed")
		os.system("TASKKILL /IM iexplore.exe")
		time.sleep(5)
	except Exception as e:
		print(e)

from webdriver_manager.chrome import ChromeDriverManager
password = "v4vijayism@"
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import gmtime, strftime
from datetime import date
from bs4 import BeautifulSoup as BS

from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
import pyperclip

client = MongoClient("mongodb+srv://sarankavalan:Saran4moziya@cluster0-oesgl.mongodb.net/twitter?retryWrites=true&w=majority")
db = client.get_database('Twitter')

driver = webdriver.Chrome(executable_path=r'C:\Users\saran-wlf\Desktop\immy\chromedriver.exe')
driver1 = webdriver.Chrome(chrome_options = option, executable_path=r'C:\Users\saran-wlf\Desktop\immy\chromedriver.exe')

def test_search_in_python_org():
    print("enter") 
    driver.get("https://twitter.com/i/flow/signup")
    
    driver1.get("https://temp-mail.org/en/")
    time.sleep(4)
    
    
    
    mail  = WebDriverWait(driver1, 20).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@data-original-title="Your Temporary Email Address"]')))
    elem = mail[0]
    elem.send_keys(Keys.CONTROL, 'a') #highlight all in box
    elem.send_keys(Keys.CONTROL, 'c') #copy
    tempMail = pyperclip.paste()
    tempName = tempMail.split("@")[0]
    name  = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@autocapitalize="sentences"]')))    
    emailbutton  = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@class="css-18t94o4 css-901oao r-1n1174f r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-19h5ruw r-bcqeeo r-qvutc0"]')))    
    name[0].send_keys(tempName)
    emailbutton[0].click()
    emailInput  = WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@name="email"]')))
    emailInput[0].send_keys(tempMail)
    
    select = Select(driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[5]/div[3]/div/div[1]/div[2]/select'))

# select by visible text
    select.select_by_visible_text('January')
    
    select = Select(driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[5]/div[3]/div/div[2]/div[2]/select'))

# select by visible text
    select.select_by_visible_text('11')
    
    select = Select(driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[5]/div[3]/div/div[3]/div[2]/select'))

# select by visible text
    select.select_by_visible_text('1992')
    time.sleep(4)
    signUp  = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div[3]/div')))
    driver.execute_script("arguments[0].click();", signUp)
    nextButton  = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div[3]/div')))
    driver.execute_script("arguments[0].click();", nextButton)
    signUpButton  = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/div')))
    driver.execute_script("arguments[0].click();", signUpButton)
    verifyButton  = WebDriverWait(driver1, 20).until(EC.presence_of_all_elements_located((By.XPATH, '/html/body/main/div[1]/div/div[2]/div[2]/div/div[1]/div/div[4]/ul/li[2]/div[2]/span/a')))
    verifyText = verifyButton[0].text.split(" ")
    code = verifyText[0]
    codeVerifyInput  = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[2]/label/div/div[2]/div/input')))
    codeVerifyInput[0].send_keys(code)
    codeVerifyInput  = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div[3]/div/div')))
    driver.execute_script("arguments[0].click();", codeVerifyInput)
    driver1.quit()
    codeVerifyInput  = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[3]/div/label/div/div[2]/div/input')))
    codeVerifyInput[0].send_keys(password)
    db.twitter.insert_one({"email":tempMail,"password":password})
    time.sleep(3)
    try:
        codeVerifyInput  = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div[3]/div/div')))
        driver.execute_script("arguments[0].click();", codeVerifyInput)
        codeVerifyInput  = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div[3]/div/div')))
        driver.execute_script("arguments[0].click();", codeVerifyInput)
        codeVerifyInput  = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[3]/label/div/div[2]/div/textarea')))
        driver.execute_script("arguments[0].textContent = 'There is no free lunch';", codeVerifyInput)
        codeVerifyInput  = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div[3]/div/div')))
        driver.execute_script("arguments[0].click();", codeVerifyInput)
        codeVerifyInput  = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div[3]/div/div')))
        driver.execute_script("arguments[0].click();", codeVerifyInput)
        codeVerifyInput  = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div[3]/div/div')))
        driver.execute_script("arguments[0].click();", codeVerifyInput)
        codeVerifyInput  = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div/div[3]/div[2]/div')))
        driver.execute_script("arguments[0].click();", codeVerifyInput)
    except Exception as e:
        print(e)
        driver.get("https://twitter.com/CaptainSaran")
        time.sleep(1)
    driver.get("https://twitter.com/CaptainSaran")
    print("16")

test_search_in_python_org()
while(True):
    try:
        driver.get('https://twitter.com/search?q=%2327YrsOfKWEmperorVijay&src=typeahead_click&f=live')
        time.sleep(10)
        driver.execute_script('''
function createElement( str ) {
    var frag = document.createDocumentFragment();

    var elem = document.createElement('div');
    elem.innerHTML = str;

    while (elem.childNodes[0]) {
        frag.appendChild(elem.childNodes[0]);
    }
    return frag;
}

var beep = (function () {
    var ctxClass = window.audioContext ||window.AudioContext || window.AudioContext || window.webkitAudioContext
    var ctx = new ctxClass();
    return function (duration, type, finishedCallback) {

        duration = +duration;

        // Only 0-4 are valid types.
        type = (type % 5) || 0;

        if (typeof finishedCallback != "function") {
            finishedCallback = function () {};
        }

        var osc = ctx.createOscillator();

        osc.type = type;
        //osc.type = "sine";

        osc.connect(ctx.destination);
        if (osc.noteOn) osc.noteOn(0); // old browsers
        if (osc.start) osc.start(); // new browsers

        setTimeout(function () {
            if (osc.noteOff) osc.noteOff(0); // old browsers
            if (osc.stop) osc.stop(); // new browsers
            finishedCallback();
        }, duration);

    };
})();

function converttomilli(dur,type)
{
    if (type=='sec')
        dur=dur*1000
    else if (type=='min')
        dur=dur*60*1000
    else if (type=='hr')
        dur=dur*60*60*1000
    else if (type=='day')
        dur=dur*24*60*60*1000    
    
    return dur;
    
}


function random_between(interval,interval2)
{
    var rand=Math.floor(Math.random()*(interval2-interval+1)+interval)
    //console.log(rand)
    return rand;
}
function get_links(){
    //var links=document.querySelectorAll('[data-testid="retweetConfirm"]')
	var links=document.querySelectorAll('[data-testid="retweet"]')
	var allinks=[]
    var button_links=[]
		for (i = 0; i < links.length; i++) {
				allinks.push(links[i])
				button_links.push(links[i])
				
			if ( i == links.length-1 || button_links.length==sd_numberofclicks)     
			   return [button_links,allinks];
		}    
}

function deletelinks(links)
{
	for (i = 0; i < links.length; i++) {
		links[i].remove()
	}
}
var sd_min_interval=converttomilli(0,'sec')
var sd_max_interval=converttomilli(1,'sec')
var sd_numberofclicks=8
var sd_no_of_errs=0
var totalcount=0
function click_links(links,deletelinksvar){
	if(links.length==0)
		deletelinks(deletelinksvar)
	for (i = 0; i < links.length; i++) {
		links[i].scrollIntoView();
		links[i].click()
		try{setTimeout(function(){document.querySelector('[data-testid="retweetConfirm"]').click()},random_between(100,1000));}catch(e){}
		sd_no_of_errs=0
		if ( i == links.length-1)
		{
			totalcount=totalcount+links.length;
			document.getElementById('igcnt').innerText= totalcount;
			deletelinks(deletelinksvar)
		}
	}
}
function main_func(){
	try{
		if(totalcount>sd_max_clicks_per_action)
			{alert('You are not permitted by developer. Contact @SaranKavalan');return;}
		var mainlinks=get_links()
		var actionlinks=mainlinks[0]
		var deletelinksvar=mainlinks[1]
		//console.log(mainlinks)
		click_links(actionlinks,deletelinksvar)
		setTimeout(function(){return main_func()}, random_between(sd_min_interval,sd_max_interval));
	}
	 catch(e){
		 sd_no_of_errs=sd_no_of_errs+1;
		 window.scrollTo(0,document.body.scrollHeight);
		 //console.log(sd_no_of_errs)
		 if(sd_no_of_errs>=6)
			beep(500, 2, function(){});
		 setTimeout(function(){return main_func()}, random_between(sd_min_interval,sd_max_interval));
	 }
}	

function addcountwidget(){  
     var p_ele2=createElement('<div align="center" style="z-index:2000;position: fixed;    top: 13em;    right: 31em;border-radius: 10px 10px;    background: #28b6de;    padding: 20px;     width: 390px;    height: 115px;" class="rcorners2"><table><tr><td align="center" style="font-size: 25px; font-family:verdana; color:white; font-weight: bold;">RETWEET BOT BY ☬SARANKAVALAN</td></tr><tr><td align="center"><span style="font-size: 35px; font-family:verdana; font-color:white; font-weight: bold;"id="igcnt">0</span></td></tr></table></div>')
    document.getElementsByTagName("body")[0].appendChild(p_ele2)

}	
var sd_max_clicks_per_action=400
var num_of_clicks=0
function getalljson(type){
try{	
chrome.storage.local.get({sd_options_storage:'{}'}, function(result) {
          var obj=JSON.parse(result.sd_options_storage)
			sd_min_interval=converttomilli(obj['sd_'+type+'_min'],'sec')
			sd_max_interval=converttomilli(obj['sd_'+type+'_max'],'sec')
			sd_numberofclicks=parseInt(obj['sd_'+type+'_rate'])
			if(parseInt(obj['sd_'+type+'_per_action'])<parseInt(Math.PI.toString().substring(4, 6)))
				sd_max_clicks_per_action=parseInt(obj['sd_'+type+'_per_action'])
			else
				sd_max_clicks_per_action=parseInt(Math.PI.toString().substring(4, 6))
			//console.log(sd_min_interval)
			//console.log(sd_max_interval)
			//console.log(sd_numberofclicks)
			//console.log(sd_max_clicks_per_action)
        });	}catch(e){}
}
getalljson('retweet')
addcountwidget()
setTimeout(function(){return main_func()}, 500);

''')
        time.sleep(200)
    except Exception as e:
        print(e)
        time.sleep(20)
