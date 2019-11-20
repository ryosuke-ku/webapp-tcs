public class Calculator {



    public double addition(double amount1, double amount2) {
        return amount1+amount2;
    }

    public double addition(double... amounts) {
        double total=0.0;
        for (double amount : amounts) {
            total+=amount;
        }
        return total;
    }

    public double subtraction(double total, double amount) {
        total -= amount;
        return total;
    }

    public double subtraction(double total, double... amounts) {
        for (double amount : amounts) {
            total-=amount;
        }
        return total;
    }

    public double multiply(Integer quantity, double cost) {
        if( quantity<0 || cost<0) return 0.0;
        return quantity *  cost ;
    }

    public Boolean multiplyByRandom(double amount) {
        Random random = new Random();
        double randomNumber=random.nextDouble();
        double result = amount*randomNumber ;
        return true;
    }
}
