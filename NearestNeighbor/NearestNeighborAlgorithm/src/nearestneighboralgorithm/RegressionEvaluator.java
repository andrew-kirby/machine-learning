package nearestneighboralgorithm;

import java.util.Iterator;

/**
 *
 * @author andy-
 */
public class RegressionEvaluator implements IEvaluator{
    
    double mse; //Holds the mean squared error
    
    double mae; //Holds the mean absolute error
    
    double me; //Holds the mean error
    
    public RegressionEvaluator(double[] predicted, Set actual) {
        int num_examples = actual.getNumExamples();
        
        mse = 0;
        mae = 0;
        me = 0;
        //---------------------------------------------------------------
        //Calculate the mean squared error and mean absolute error
        int index = 0;
        Iterator<Example> iterator = actual.iterator();
        while(iterator.hasNext()) {
            double difference = predicted[index] - iterator.next().getValue();
            me += difference;
            mae += Math.abs(difference);
            mse += Math.pow(difference, 2);
            index++;
        }
        //Take the average
        mse /= num_examples;
        mae /= num_examples;
        me /= num_examples;
    }
    
    @Override
    public double getAccuracy() {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public double getMSE() {
        return mse;
    }

    @Override
    public double getMAE() {
        return mae;
    }
    
    @Override
    public double getME() {
        return me;
    }
}