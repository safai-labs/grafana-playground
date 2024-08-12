from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import csv
import io

app = FastAPI()

@app.get('/stats')
def get_stats():
    output = io.StringIO()
    writer = csv.writer(output)

    # Replace with your data fetching and writing logic
    writer.writerow(['Header1', 'Header2', 'Header3'])
    writer.writerow(['Value1', 'Value2', 'Value3'])

    output.seek(0)
    return StreamingResponse(io.StringIO(output.getvalue()), media_type='text/csv')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
