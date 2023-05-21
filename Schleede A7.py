stocks_dict = {
  "APL" : "APL is $257",
  "IBM":"IMB is $103",
  "SNDL":"SNDL is $7",
  "AMZN":"AMZN is $300",
  "NFLX":"NFLX is $138",
  "MSFT":"MSFT is $289",
  "UBR":"UBR is $113",
  "SONY":"SONY is $184",
  "WAL":"WAL is $201",
  "UHC":"UHC is $567",
  "GOOG":"GOOG is $360",
  "TSLA":"TSLA is $394",
  "SNAP":"SNAP is $300"
}
x = input("Please enter your desired stock symbol: ")
y = stocks_dict.get(x, "Your entered stock symbol wasn't recognized.")
print(y)