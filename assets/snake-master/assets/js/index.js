function choose_difficulty(maze_type)
{
    if(maze_type == null)
    {
        window.location.href = "/"
    }
    else
    {
        window.location.href = "/Snake_Master/difficulty?maze=" + maze_type
    }
}

function choose_challenge_type(challenge,increment, speed)
{
    if(increment == null || speed == null || challenge ==  null)
    {
        window.location.href = "/"
    }
    else
    {
        window.location.href = "/Snake_Master/" + challenge + "?increment=" +  increment + "&speed=" +  speed
    }
}