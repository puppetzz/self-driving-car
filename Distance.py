class Distance:
    traffic_light = ['green_light', 'red_light']
    
    @staticmethod
    def get_result(model, image):
        final_results = []
        results = model(image)
        for i, row in results.pandas().xyxy[0].iterrows():
            confidence = float(row["confidence"])
            name = str(row["name"])
            xmin, ymin, xmax, ymax = (
                int(row["xmin"]),
                int(row["ymin"]),
                int(row["xmax"]),
                int(row["ymax"]),
            )
            final_results.append((name, confidence, xmax - xmin, ymax - ymin))
        return final_results
    
    @staticmethod
    def get_traffic_light_distance(data):
        name = data[0][0]
        if not name in Distance.traffic_light:
            return None
        confidence = data[0][1]
        width = data[0][2]
        W = 1.6
        f = 265
        return (W * f) / width
        
        