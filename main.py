import os
import http.server
import socketserver
from datetime import datetime

class SimpleHTMLHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>AI Fraud Dashboard - Simplified</title>
            <style>
                body {{
                    font-family: 'Helvetica Neue', Arial, sans-serif;
                    line-height: 1.6;
                    color: #f5f5f5;
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 20px;
                    background-color: #222526;
                }}
                .container {{
                    background-color: #353A3E;
                    padding: 30px;
                    border-radius: 8px;
                    box-shadow: 0 2px 10px rgba(0,0,0,0.3);
                }}
                h1 {{
                    color: #e0e0e0;
                    border-bottom: 2px solid #0071e3;
                    padding-bottom: 10px;
                }}
                .card {{
                    border: 1px solid #444;
                    border-radius: 8px;
                    padding: 20px;
                    margin-bottom: 20px;
                    background-color: #1A1A1A;
                }}
                .success {{
                    color: #34c759;
                    font-weight: bold;
                }}
                .warning {{
                    color: #ff9500;
                    font-weight: bold;
                }}
                .grid {{
                    display: grid;
                    grid-template-columns: repeat(2, 1fr);
                    gap: 20px;
                    margin-top: 30px;
                }}
                .chart {{
                    border: 1px solid #444;
                    border-radius: 8px;
                    height: 300px;
                    display: flex;
                    flex-direction: column;
                    justify-content: space-between;
                    padding: 15px;
                    background-color: #1A1A1A;
                }}
                .chart-title {{
                    color: #e0e0e0;
                    text-align: center;
                    margin-bottom: 10px;
                }}
                .chart-bar {{
                    background-color: #0071e3;
                    margin-bottom: 10px;
                    border-radius: 4px;
                    position: relative;
                    color: white;
                    text-align: right;
                    padding-right: 10px;
                    font-weight: bold;
                }}
                .chart-label {{
                    display: flex;
                    justify-content: space-between;
                    color: #bfbfbf;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>AI Fraud Intelligence Dashboard</h1>
                <p>Simplified static version</p>
                
                <div class="card">
                    <h2 class="success">Server Successfully Deployed!</h2>
                    <p>This version is running on pure Python without any dependencies.</p>
                    <p>Current time: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
                    <p>Running on port: {os.environ.get("PORT", "8080")}</p>
                </div>
                
                <div class="card">
                    <h3 class="warning">Next Steps</h3>
                    <p>We're successfully serving content, which means Railway deployment is working. From here:</p>
                    <ol>
                        <li>Use a simpler stack with compatible dependencies</li>
                        <li>Consider splitting your application into smaller services</li> 
                        <li>Implement one feature at a time to identify compatibility issues</li>
                    </ol>
                </div>
                
                <div class="grid">
                    <div class="chart">
                        <h3 class="chart-title">Sample AI Fraud Categories</h3>
                        <div style="flex-grow: 1; display: flex; flex-direction: column; justify-content: flex-end;">
                            <div class="chart-bar" style="width: 70%; height: 35px;">35</div>
                            <div class="chart-bar" style="width: 50%; height: 35px;">25</div>
                            <div class="chart-bar" style="width: 80%; height: 35px;">40</div>
                            <div class="chart-bar" style="width: 40%; height: 35px;">20</div>
                            <div class="chart-bar" style="width: 60%; height: 35px;">30</div>
                        </div>
                        <div class="chart-label">
                            <span>Deepfake</span>
                            <span>Voice Clone</span>
                            <span>AI Phishing</span>
                            <span>Identity Theft</span>
                            <span>Financial</span>
                        </div>
                    </div>
                    
                    <div class="chart">
                        <h3 class="chart-title">Risk Levels</h3>
                        <div style="flex-grow: 1; display: flex; flex-direction: column; justify-content: flex-end;">
                            <div class="chart-bar" style="width: 30%; height: 35px; background-color: #ff3b30;">15</div>
                            <div class="chart-bar" style="width: 60%; height: 35px; background-color: #ff9500;">30</div>
                            <div class="chart-bar" style="width: 90%; height: 35px; background-color: #ffcc00;">45</div>
                            <div class="chart-bar" style="width: 20%; height: 35px; background-color: #34c759;">10</div>
                        </div>
                        <div class="chart-label">
                            <span>Critical</span>
                            <span>High</span>
                            <span>Medium</span>
                            <span>Low</span>
                        </div>
                    </div>
                </div>
            </div>
        </body>
        </html>
        """
        
        self.wfile.write(html_content.encode('utf-8'))

def run_server():
    port = int(os.environ.get('PORT', 8080))
    print(f"Starting server on port {port}")
    
    handler = SimpleHTMLHandler
    httpd = socketserver.TCPServer(("", port), handler)
    
    print(f"Server running at http://0.0.0.0:{port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()
