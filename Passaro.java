package model;

public class Passaro extends Animal {

    public Passaro(String nome) {
        super(nome);
    }

    public String emitirSom() {
        return "Piu piu!";
    }
}
