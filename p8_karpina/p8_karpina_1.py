import re

pose_estimation = "[BodyPart:0-(0.55, 0.17) score=0.81 BodyPart:1-(0.49, 0.27) score=0.85 BodyPart:2-(0.41, 0.26) score=0.67 BodyPart:3-(0.33, 0.37) score=0.72 BodyPart:4-(0.36, 0.48) score=0.78 BodyPart:5-(0.58, 0.27) score=0.81 BodyPart:6-(0.65, 0.38) score=0.88 BodyPart:7-(0.62, 0.48) score=0.86 BodyPart:8-(0.43, 0.48) score=0.60 BodyPart:9-(0.43, 0.66) score=0.67 BodyPart:10-(0.53, 0.79) score=0.56 BodyPart:11-(0.53, 0.48) score=0.56 BodyPart:12-(0.59, 0.66) score=0.75 BodyPart:13-(0.49, 0.80) score=0.50 BodyPart:14-(0.54, 0.15) score=0.73 BodyPart:15-(0.56, 0.15) score=0.85 BodyPart:16-(0.48, 0.16) score=0.81 BodyPart:17-(0.83, 0.18) score=0.79]"
pattern_points = re.compile(r"\(([^()]+)\)")
pattern_scores = re.compile(r"\s[a-zA-Z]*=(\d.\d+)")

match_points = re.findall(pattern_points, pose_estimation)
match_scores = re.findall(pattern_scores, pose_estimation)
points = [float(i) for s in match_points for i in s.split(", ")]
scores = [float(i) for i in match_scores]

print(f"{points=}")
print(f"{scores=}")