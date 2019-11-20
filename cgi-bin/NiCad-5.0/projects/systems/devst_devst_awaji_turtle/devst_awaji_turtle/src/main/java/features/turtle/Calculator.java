public class Calculator {





	public String execute(String fomula) {
		// TODO 自動生成されたメソッド・スタブ
		//String fomula = "1+3";
		//System.out.println(getOperator(fomula));
		String strToken = getOperator(fomula);
		String[] strAry = fomula.split(strToken);
		//String[] strAry = fomula.split("\\+");

		int firstValue = Integer.valueOf(strAry[0]).intValue();
		int secondValue = Integer.valueOf(strAry[1]).intValue();

		BigDecimal result = calOperator(strToken,firstValue, secondValue);
		//System.out.println(result);
		return result.toString();
	}










































}
