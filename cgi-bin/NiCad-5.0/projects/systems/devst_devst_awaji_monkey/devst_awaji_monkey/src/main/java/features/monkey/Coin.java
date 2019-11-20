public class Coin {






	public String coinUsage(int amount) {
		if (amount <= 0) {
			throw new RuntimeException();
		}
		int[] numbers = new int[6];
		int i = 0;
		for (int coin : COINS) {
			numbers[i] = amount / coin;
			amount -= numbers[i] * coin;
			i++;
		}
		return format(numbers);
	}

	private String format(int[] numbers) {
		String result = "";
		int i = 0;
		for (int coin : COINS) {
			if (numbers[i] != 0) {
				if (!result.isEmpty()) {
					result += "と";
				}
				result += coin + "円玉";
				if (numbers[i] > 1) {
					result += numbers[i] + "枚";
				}
			}
			i++;
		}
		return result;
	}
}
