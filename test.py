# from vncorenlp import VnCoreNLP
# annotator = VnCoreNLP(address="http://127.0.0.1", port=9000) 
import VietnameseTextNormalizer

# Input 
text = "Warren Edward Buffett sinh ngày 30 tháng 8 thùy thuỳ năm 1930 tại Omaha,"

a = VietnameseTextNormalizer.Normalize(text)
f = open("a.txt", 'w')
f.write(a)