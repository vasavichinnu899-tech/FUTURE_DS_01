import java.io.*;
import java.util.*;

class Sale {
    int id;
    String customer;
    String product;
    String region;
    int qty;
    int price;
    String date;

    public Sale(int id, String customer, String product, String region,
                int qty, int price, String date) {
        this.id = id;
        this.customer = customer;
        this.product = product;
        this.region = region;
        this.qty = qty;
        this.price = price;
        this.date = date;
    }

    public int getRevenue() {
        return qty * price;
    }
}

public class Main {
    public static void main(String[] args) {

        ArrayList<Sale> sales = new ArrayList<>();

        
        try {
            Scanner sc = new Scanner(new File("sales.txt"));

            while (sc.hasNextLine()) {
                String line = sc.nextLine();
                String[] p = line.split(",");

                Sale s = new Sale(
                        Integer.parseInt(p[0]),
                        p[1],
                        p[2],
                        p[3],
                        Integer.parseInt(p[4]),
                        Integer.parseInt(p[5]),
                        p[6]
                );

                sales.add(s);
            }

            sc.close();

        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }

       
        int totalRevenue = 0;
        for (Sale s : sales) {
            totalRevenue += s.getRevenue();
        }

       
        HashMap<String, Integer> productMap = new HashMap<>();
        for (Sale s : sales) {
            productMap.put(s.product,
                    productMap.getOrDefault(s.product, 0) + s.qty);
        }

        String topProduct = "";
        int maxQty = 0;

        for (String key : productMap.keySet()) {
            if (productMap.get(key) > maxQty) {
                maxQty = productMap.get(key);
                topProduct = key;
            }
        }

       
        HashMap<String, Integer> customerMap = new HashMap<>();
        for (Sale s : sales) {
            customerMap.put(s.customer,
                    customerMap.getOrDefault(s.customer, 0) + s.getRevenue());
        }

        String topCustomer = "";
        int maxSpent = 0;

        for (String key : customerMap.keySet()) {
            if (customerMap.get(key) > maxSpent) {
                maxSpent = customerMap.get(key);
                topCustomer = key;
            }
        }

       
        HashMap<String, Integer> regionMap = new HashMap<>();
        for (Sale s : sales) {
            regionMap.put(s.region,
                    regionMap.getOrDefault(s.region, 0) + s.getRevenue());
        }

        String topRegion = "";
        int maxRegion = 0;

        for (String key : regionMap.keySet()) {
            if (regionMap.get(key) > maxRegion) {
                maxRegion = regionMap.get(key);
                topRegion = key;
            }
        }

       
        List<Map.Entry<String, Integer>> productList =
                new ArrayList<>(productMap.entrySet());

        productList.sort((a, b) -> b.getValue() - a.getValue());

        
        List<Map.Entry<String, Integer>> customerList =
                new ArrayList<>(customerMap.entrySet());

        customerList.sort((a, b) -> b.getValue() - a.getValue());

      
        HashMap<String, Integer> monthMap = new HashMap<>();

        for (Sale s : sales) {
            String month = s.date.substring(0, 7);
            monthMap.put(month,
                    monthMap.getOrDefault(month, 0) + s.getRevenue());
        }

        
        System.out.println("\n==================================");
        System.out.println("      SALES ANALYTICS DASHBOARD   ");
        System.out.println("==================================");

        System.out.println("\nTOTAL REVENUE: " + totalRevenue);
        System.out.println("TOP PRODUCT: " + topProduct);
        System.out.println("TOP CUSTOMER: " + topCustomer);
        System.out.println("TOP REGION: " + topRegion);

      
        System.out.println("\nTOP 5 PRODUCTS:");
        for (int i = 0; i < Math.min(5, productList.size()); i++) {
            System.out.println((i + 1) + ". " +
                    productList.get(i).getKey() + " -> " +
                    productList.get(i).getValue());
        }

        
        System.out.println("\nTOP 5 CUSTOMERS:");
        for (int i = 0; i < Math.min(5, customerList.size()); i++) {
            System.out.println((i + 1) + ". " +
                    customerList.get(i).getKey() + " -> " +
                    customerList.get(i).getValue());
        }

      
        System.out.println("\nMONTHLY TREND:");
        for (String m : monthMap.keySet()) {
            System.out.println(m + " -> " + monthMap.get(m));
        }

        System.out.println("\n==================================");
    }
}