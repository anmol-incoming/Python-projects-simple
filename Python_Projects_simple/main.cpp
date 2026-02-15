//
//  main.cpp
//  Practice.cpp
//
//  Created by Anmol Sharma on 14/02/26.
//
/* It's a Simple battleship game. Where user has to guess a row and column,if selected a row and column where ship S is there then it's a hit else it's a miss.Hit is shown by letter 'X',while miss is shown by letter 'O'.Water is shown by letter '~' and lastly ship is shown by letter 'S'.In the end the result is displayed after the 8 chances are complted. If all ships hit before 8 chances, you are decleared as a winner.
 */
#include<iostream>
#include<string>

int main(){
    char board[5][4]={
        {'~','~','S','~'},
        {'S','~','~','S'},
        {'~','~','~','~'},
        {'~','~','~','~'},
        {'S','~','S','~'}
    };
    int chances=8,total_ships=5;
    
    int row,column;
    
    std::cout<<"Welecome to the game of Battleship,where you have select rows and columns 5X4 matrix."<<"\n";
    while (chances!=0)
    {
        if(total_ships!=0)
        {
            std::cout<<"Select the row:-";
            std::cin>>row;
            std::cout<<"Select the column-";
            std::cin>>column;
            if(board[row-1][column-1]=='S')
            {
                std::cout<<"Hurray!! It's a HIT. "<<"\n";
                board[row-1][column-1]='X';
                total_ships-=1;
                std::cout<<"Total ship left= "<<total_ships<<"\n";
            }
            else if(board[row-1][column-1]=='~')
            {
                std::cout<<"Oops !! It's a miss .Please try again."<<"\n";
                board[row-1][column-1]='O';
            }
            else{
                std::cout<<"Invalid row and column number."<<"\n";
                std::cout<<"Total ship left= "<<total_ships<<"\n";
                
            }
            
        }
        else
        {
            std::cout<<"Hurray!! You won Chapmion. "<<"\n";
            break;
        }
        chances-=1;
        std::cout<<"Total chances left= "<<chances<<"\n";
    }
    for(int j=0;j<5;j++){
        for(int k=0;k<4;k++){
            std::cout<<"Final result is shown below-"<<"\n"<<board[j][k]<<" ";
            
        }
        std::cout<<"\n";
    }
}
