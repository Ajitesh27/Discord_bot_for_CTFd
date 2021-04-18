<?php
function get_rows() {
$file=fopen("scoreboard.txt",'r');
while($line = fgets($file)){
	$line=trim($line);
	list($serial,$team,$points,$solves) = explode('|',$line);
	echo "<tr><td align=\"center\">$serial</td><td align=\"center\">$team</td><td align=\"center\">$solves</td><td align=\"center\">$points</td></tr>\n";
}
return true;
}
?>



<!doctype html>
<html lang="en">
  <head>    
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
    <script src="https://kit.fontawesome.com/836aa845a8.js" crossorigin="anonymous"></script>
    <link rel='stylesheet' href='style.css'>
    <style>
.tab {
    display: inline-block;
    margin-left: 900px;
}
</style>
    <title>Discord Bot Dashboard</title>
  </head>
  <body>
    <div class = 'container-fluid'>
        
        <div class = 'row' id = 'main_body'>

<!-- the left navigation  -->

            <div class = 'col-2 p-2 bg-dark text-light shadow-lg' id = 'left_navigation'>
<a href='https://discord.com/'>               
 <img src="discord.jpg" height="200" width="250" ></a>
                
                <p class='text-muted mt-2'><small>PES OOAD Project </small></p>



<!-- side bar navigation  -->

                <div id = 'menu_nav'>
                    <ul>
                        <li href="index.html">
                           
                            
                            <span> Tasks </span>
                            <br>
                            <ul class = 'my-2'>
                                <li>
                                    <a href='https://discord.com/channels/827925862472613888/827929037094912020' onclick="view_categories()">View Categories</a>
                                </li>
                                <li>
                                    <a href='https://discord.com/channels/827925862472613888/827929037094912020' onclick="view_challenges()">View Challenges</a>
                                </li>
                                <li>
                                    <a href='https://discord.com/channels/827925862472613888/827929037094912020' onclick="Add challenges()">Add Challenges</a>
                                </li>
                                
                            </ul>
                        </li>
                    </ul>
                    <br>
                    <ul>
                        <li>
                            
                            <span> Support </span>
                            <br>
                            <ul class = 'my-2'>
                                <li>
                                    <a href='help.html' onclick="help()">Help Manual</a>
                                </li>
                                
                            </ul>
                        </li>
                    </ul>
                    

                </div>

            </div>

<!-- the main data display area -->

            <div class = 'col-10 p-2 bg-light shadow-lg float-left' id = 'work_area'>

                <h1 class = 'text-center text-muted'>CTF Dashboard</h1>
                <h1 class = 'text-center text-muted'>Score card</h1>

<!-- the top navigation -->

                <div>
 
                   <span class="tab"></span>
                   <button type="button"  id='button_issue' onclick="location.href='login.html';" class="btn btn-primary mt-4" data-toggle="modal" data-target="#issue_reg" float='right'>Log Out</button>
                </div>


<!-- start of the table display -->

                <div>
                    <table class="table table-striped mt-4">
                        <thead class="thead-dark">
                        <tr>
                            <th class="text-center">Rank</th>
                            <th class="text-center">Team Name</th>
                            <th class="text-center">Number of Solves</th>
                            <th class="text-center">Points</th>
                            
                           
                            
                        </tr>
                        </thead>
                        <tbody id = 'table'>

                        <?php get_rows(); ?>
                    </table>
                </div>



<!-- canvas - ball bouncing location -->

<canvas id="canvas" width="1368" height="798"></canvas>
    
<!-- bootstrap JS and the main JS file -->
    
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>
    <script type='text/javascript' src='script.js'></script>
</body>
