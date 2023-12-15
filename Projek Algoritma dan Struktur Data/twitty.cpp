#include <iostream>
#include <string>

/**
 * 215150300111043_Nadaa Shafa Nadhifa
 * 215150301111035_Ni Made Ayu Astina Sari
 * 215150301111037_Talitha Dwi Arini
 */

using namespace std;
int sub = 0;
int well= 1;
int noun = 0;

struct twitty{
    string username;
    string grouptopic[3];
    int connection;
    int participator;
    int participate[100];
    void insert(string nama, string topik[3]);
    void follow(string nama1, string nama2);
    string mostfollow();
    int minretwit(string nama1, string nama);
};

void insert(string username, string grouptopic[3]){
    twitty data[100];
    data[sub].username = username;
    data[sub].connection = 0;
    data[sub].grouptopic[0] = grouptopic[0];
    data[sub].grouptopic[1] = grouptopic[1];
    data[sub].grouptopic[2] = grouptopic[2];
    for (int i=0;i<100;i++){
        data[sub].participate[i]=0;
    } noun++;
    data[sub].participator = 0;
    sub++;
}

void connect(string user1, string user2){
    twitty data[100];
    int space1=1, space2=2;
    for(int i=0;i<sub;i++){
        if(data[i].username==user1){
            space1=1;
        } 
    }if(space1!=1){
        for(int i=0;i<sub; i++){
            if(data[i].username==user2){
                data[space1].participate[i]=1;
                data[i].participator++;
                if(data[space1].connection==0 || data[i].connection==0){
                    noun--;
                    int exist=0;
                    if(data[space1].connection==0 && data[i].connection==0){
                        data[space1].connection = well;
                        data[i].connection = well;
                        well++;
                    } else {
                        if (data[space1].connection!=0){
                            data[i].connection = data[space1].connection;
                        } else {
                            data[space1].connection = data[i].connection;
                        }
                    }
                }
            }
        }
    }
}

string grouptopic(){
    twitty data[100]; 
    string str="";
    for(int x=0; x<well; x++){
        int hobby=0;
        int temp [sub];
        int bin = 0;
        for(int y=0; y<sub; y++){
            if(data[y].connection==x){
                temp[bin] = y;
                bin++;
            }
        }
        for(int z=0; z<3; z++){
            int check = 1;
            for(int t=1; t<bin; t++){
                int p = 0;
                for(int l=0; l<3; l++){
                    if(data[temp[0]].grouptopic[z]==data[temp[t]].grouptopic[l]){
                        p=1;
                    }
                }
                if(p==0){
                    check=0;
                    break;
                }
            }
            if(check==1){
                if(hobby!=0){
                    str+=",";
                }
                str+=data[temp[0]].grouptopic[z];
                hobby++;
            }
        }
        str+="\n";
    }
    return str;
}

string mostfollow(){
    twitty data[100];
    int max = 0;
    string username = "";
    for(int i=0;i<sub;i++){
        if(data[i].participator>max){
            max = data[i].participator;
            username = data[i].username;
        }
    }
    return username;
}

int minretwit(string user1, string user2){
    twitty data[100];
    int space1 = -1, space2 = -1;
    int total = -1;
    for(int i=0;i<sub;i++){
        if(data[i].username==user1){
            space1 = i;
        }
    }
    for(int i=0;i<sub;i++){
        if(data[i].username==user2){
            space2 = 1;
        }
    }
    if (data[space1].participate[space2]==1){
        total++;
    }
    for(int i=0;i<sub;i++){
        if(data[space1].participate[i]==1&&i!=space2){
            for(int t=0;t<sub;t++){
                if(data[i].participate[t]==1&&t!=space2){
                    if(data[t].username[space2]==1){
                        total++;
                    }
                }
            }
            if(data[i].username[space2]==1){
                total++;
            }
        }
    }
    return total;
}

int main(){
    int z=0;
    int sub=0;
    cin >> z;
    cin >> sub;
    for(int i=0;i<z;i++){
        string username,data[3];
        cin >> username;
        cin >> data[0];
        cin >> data[1];
        cin >> data[2];
        insert(username,data);
    }
    for (int t=0;t<sub;t++){
        string input;
        cin >> input;
        if(input=="mostfollow"){
            cout << mostfollow() <<endl;
        } else if (input=="insert"){
            string username,data[3];
            cin >> username;
            cin >> data[0];
            cin >> data[1];
            cin >> data[2];
            insert(username,data);
            cout << username << "inserted\n";
        } else if (input=="grouptopic"){
            cout << grouptopic() << endl;
        } else if (input=="noun"){
            cout << noun << endl;
        } else if  (input=="minretwit"){
            string username, username2;
            cin >> username;
            cin >> username2;
            cout << minretwit(username,username2)<<endl;
        }
    }
    system("pause");
}
