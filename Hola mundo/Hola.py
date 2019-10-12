//Programa de ejemplo para arduino

int botonA = 2;
int botonB = 3;
int led = 4;
void setup(){
    //Establecer condiciones de trabajo o iniciales
    pinMode(botonA,INPUT)
    pinMode(botonB,INPUT)
    pinMode(led,OUTPUT)
}

void loop(){
    //Funcion  principal
    if(digitalRead(botonA) && digitalRead(botonB)){
        digitalWrite(led, 1);
    }else{//Usar HIGH o LOW
        digitalWrite(led,0);
    }
}