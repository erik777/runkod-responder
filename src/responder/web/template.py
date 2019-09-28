base_temp = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>Runkod</title>
    <style>
    body{
        background-color: #007bff;
        color: #fff;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial;
        font-size: 1rem;
        position: absolute;
        left:0;
        top:0;
        width:100%;
        height: 100%;
        margin:0;
    }
    
    .content{
        display: flex;
        align-items:center;
        justify-content:center;
        flex-direction: column;
        width:100%;
        height: 100%;
    }
    
    .content .message{
        font-size: 30px;
        text-align: center;
    }

    .content .logo{
        width:200px;
        height: 200px;
        background: url('https://runkod.com/logo.png');
        background-size: 100%;
        margin-bottom: 10px;
    }
    </style>
  </head>
  <body>
    <div class="content">
       <div class="logo"></div>
       <p class="message"><--content--></p>
    </div>
  </body>
</html>
"""

no_project = base_temp.replace('<--content-->', 'Nothing here')

no_file = base_temp.replace('<--content-->', 'No such a resource')

in_maintenance = base_temp.replace('<--content-->', ' In Maintenance <br/><br/> Please check back shortly')
