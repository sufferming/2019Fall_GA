# vision
PecuLab in SCU FinTech


# AWS Serverless with zappa
[AWS_Serverless_with_zappa](https://github.com/aaa123848/AWS_Serverless_with_zappa?fbclid=IwAR3yns-z-jfLTpxUXZoT8iGZ17XsVHY9_9YnGggCr3cD3u1fZL8FBQt-Aeo "Title") 
writed by [aaa123848](https://github.com/aaa123848 "Title") 

# implement
1, git clone https://github.com/pecu/vision.git </br>
2, cd vision

## Two way:

3-1, 

	python new_vision -f1 "GSPC.csv" -f2 "SP500BDT.csv" -f3 "USDX.csv" -ww1 0.5 -ww2 0.25 -ww3 0.25

or 

3-2, 

## 檔案都放在一起，主程式內指令

	from vision import first_fund
	first_fund("GSPC.csv位置","SP500BDT.csv位置","USDX.csv位置",0.5,0.25,0.25).__call__("GSPC.csv","SP500BDT.csv","USDX.csv",GSPC權重,SP500BDT權重,USDX權重)

# portfolio
### 2019.12.10 新增指數、指標
## index
1,GSPC(S&P500大盤指數)</br>
2,SP500BDT(S&P500公司債指數)</br>
3,USDX(美元指數)</br>
## benchmark
1,sharp_ratio</br>
2,sortino_ratio</br>
3,excess</br>
4,var</br>
5,E on VaR</br>
#### 資料來源：Lipper/Yahoo finance

#### 2019.12.15 writed by [sufferming](https://github.com/sufferming "Title") 
