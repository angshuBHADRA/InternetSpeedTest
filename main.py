import speedtest

st= speedtest.Speedtest()
print("Your download speed is" ,st.download()//10**6, "mbps")
print("Your upload speed is" ,st.upload()//10**6, "mbps")
print("Your ping" ,int(st.results.ping),  "MS")