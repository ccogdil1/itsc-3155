#!/bin/bash

echo -n "Do you agree with this? [yes or no]: "
read yno
case $yno in
        [yY] | [y][e][s] )
                echo "Agreed"
                ;;
        [nN] | [n][o] )
                echo "Not agreed, you can't proceed the installation";
                ;;
        *) 
                echo "Invalid input"
                ;;
esac