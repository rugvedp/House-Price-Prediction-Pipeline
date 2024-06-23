from flask import Flask,request,render_template

from src.pipeline.predictions_pipeline import PredictPipeline,CustomData

app=Flask(__name__)


@app.route("/",methods=["GET","POST"])
def predict_datapoint():
    if request.method=="GET":
        return render_template("index.html")
    else:
        data=CustomData(
            area=int(request.form.get("area")),
            bedrooms=int(request.form.get("bedrooms")),
            bathrooms=int(request.form.get("bathrooms")),
            stories=int(request.form.get("stories")),
            parking=int(request.form.get("parking")),
            mainroad=request.form.get("mainroad"),
            basement=request.form.get("basement"),
            furnishingstatus=request.form.get("furnishingstatus")
        )
        final_data=data.get_data_as_dataframe()

        predict_pipeline=PredictPipeline()

        pred=predict_pipeline.predict(final_data)

        result=round(pred[0],2)

        return render_template("result.html",final_result=result)



if __name__=="__main__":
    app.run(host="0.0.0.0",port=8000)