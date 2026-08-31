package model;

public class Cachorro extends Animal {

    public Cachorro(String nome) {
        super(nome);
    }

    public String emitirSom() {
        return "Au au!";
    }
}
