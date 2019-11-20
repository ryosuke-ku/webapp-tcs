public class Probability {

































    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;

        Probability that = (Probability) o;

        BigDecimal thisValue=new BigDecimal(value).round(MathContext.DECIMAL32);
        BigDecimal otherValue=new BigDecimal(that.value).round(MathContext.DECIMAL32);
        return thisValue.equals(otherValue);

    }

    public Probability complement() {
        return new Probability(1-this.value);

    }

    public  Probability combineProbabilityWithAND(Probability other) {
        return new Probability(value * other.value);
    }

    public Probability combineProbabilityWithOR(Probability other) {
        Probability complementThis = this.complement();
        Probability complementOther = other.complement();
        Probability ANDedProbabilities = complementThis.combineProbabilityWithAND(complementOther);
        return ANDedProbabilities.complement();
        //return new Probability(other.value+this.value - this.value*other.value);
    }
}
