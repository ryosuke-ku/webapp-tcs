public class Dice {





    public double getDiceRollingProbability(int rolledNo) {
        if(rolledNo<1||rolledNo>6){
            return 0.0;
        }
        return 1/this.dicePossibilities;
    }
}
