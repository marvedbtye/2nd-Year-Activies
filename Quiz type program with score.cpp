#include <iostream>
#include <string>
using namespace std;
int main(){
	
	int guess;
	int total;
	
	class Question {
		
		private:
			string Question_Text;
			string Answer_1;
			string Answer_2;
			string Answer_3;
			string Answer_4;
			
			int Correct _Answer;
			int Question_Score;
			
		public:
			void setValues (string, string, string, string, string, int, int);
			void askQuestion ( );
	};
	
	int main (){
		coit<<"Please Enter to start the quiz..."<< endl;
		cin.get();
		
		string Name;
		int age;
		cout<<"What's your name?"<<endl;
		cin>>Name;
		cout<<endl;
		
		cout<<"How old are you?"<<endl;
		cin>>Age;
		cout<<endl;
		
		string Respond;
		cout<<"Are you ready to take the Quiz"<<Name<<"?Yes/No."<<endl;
		cin>>Respond;
		if (Respond == "Yes"){
			cout<<endl;
			cout<<"Ok, Good luck!"<<endl;
			cout<<endl;
		}
		
		else {
			cout<<"Ok, Goodbye!"<<endl;
			return 0;
		}
	Question q1;
	Question q2;
	Question q3;
	Question q4;
	Question q5;
	
	q1.setValues("How many companions did frodo have in the Fellowship of the Ring?",
			"5 Companions",
			"9 Companions",
			2,
			10);
			
	q2.setValues("Which member fought the Balrog at Moira?",
			"Gandalf",
			"Legolas",
			1,
			10);
			
	q3.setValues("How old was Aragorn when he was made King of Gondor and Arnor?",
			"87",
			"100",
			1,
			10);
	
	q4.setValues("How many were the hobbits that came with gandalf?",
			"4",
			"6",
			1,
			10);
			
	
	q5.setValues("What year of the S.A was Sauron defeated?",
			"3019",
			"3044",
			1,
			10);
			
	q1.askQuestion();
	q2.askQuestion();
	q3.askQuestion();
	q4.askQuestion();
	q5.askQuestion();
	
		cout<<"Your Total score is" << "out of 50" <<endl;
		cout<<endl;
		
		if (Total>=30){
			cout<<"You passed!"<<endl;
		}		
		
		else {
			cout<<"Sorry, you failed the quiz."<<endl;
			cout<<endl;
			cout<<"Better luck next time!"<<endl;
		}
		
		return 0;	
	}
}
